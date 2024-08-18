# MeAndMyGirl-CTF-Creds-Harvester
A not so robust script for harvesting the credentials of the Me and My Girlfriend CTF's web app accounts. The script achieves this by exploiting the parameter tampering privilege escalation flaw at `http://x.x.x.x/index.php?page=profile&user_id=x`.

# Usage
#### Obtain authenticated session cookie
**Option 1:** Register an account, then login and copy the session cookie's value from your network tab of the developer tools.
**Option 2:** Navigate to `http://x.x.x.x/misc/process.php?act=login` the app will bypass login, then copy the session cookie's value from your network tab of the developer tools.

#### Run scrape.py
```
python3 scrape.py 192.168.56.123 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 5
python3 scrape.py 192.168.56.123:8080 -sessid r4irnlb966u3b7a6sv0iupc1m4 -suid 1 -euid 5
```
**Note:** The first argument to the script should be the address of the VM.
