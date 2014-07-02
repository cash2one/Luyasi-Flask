import json
import urllib
import urllib2
import re

def login():
    loginurl = 'http://localhost:5000/security/login'

    getloingInfo = urllib2.Request(loginurl)
    res = urllib2.urlopen(getloingInfo)

    # 找到session
    session = res.headers.get('set-cookie', None)
    # 找到csrf_token
    content = res.read()

    pattern = '<input id="csrf_token" name="csrf_token" type="hidden" value="([\w\.#]+)">'

    match = re.search(pattern, content)
    csrf_token = match.group(1)
    print 'csrf_token:', csrf_token

    return

    # contacturl= 'http://localhost:5000/qingbank/contact/2'
    data = {'email':'kinorsi@gmail.com', 'password':'luyasi'}
    # toStr = 'WyIxIiwiMjUzNzM3NjRjNTQ2M2MwYzFhNjhlOThjOTUyZDBmMTYiXQ.BZ58zQ.ccD0NuGbc2kIVQVl7Cj7UGfcfYQ'
    # token = urllib.urlencode({'auth_token': toStr})
    # print token
    jdata = json.dumps(data);
    loginReq = urllib2.Request(loginurl, jdata, {'Content-Type': 'application/json'})
    # contactReq = urllib2.Request(contacturl, token)
    # contactReq.add_header('auth_token', toStr)
    # print contactReq.header_items()
    loginRes = urllib2.urlopen(loginReq)
    # contactRes = urllib2.urlopen(contactReq)

    print loginRes.read()
    # print contactRes.read()

def contact():
    toStr = 'WyIxIiwiMjUzNzM3NjRjNTQ2M2MwYzFhNjhlOThjOTUyZDBmMTYiXQ.Bb4w0g.Q2hbhUpM90dexPHBDOc1OCRlTTc'
    contacturl= 'http://localhost:5000/api/qingbank/contact/2?auth_token='+toStr
    # token = urllib.urlencode({'auth_token': toStr})
    # print token
    contactReq = urllib2.Request(contacturl)
    # contactReq.add_header('auth_token', toStr)
    # print contactReq.header_items()
    contactRes = urllib2.urlopen(contactReq)

    print contactRes.read()

login()