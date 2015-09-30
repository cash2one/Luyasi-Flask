import json
import urllib
import urllib2
import re

import requests

def login():
    loginurl = 'http://127.0.0.1:5000/security/login'

    res = requests.get(loginurl)
    print 'cookies:', res.headers['set-cookie']
    content = res.text
    cookies = res.cookies #Must send back the cookies, or the server can't make correct crsf_token

    pattern = '<input id="csrf_token" name="csrf_token" type="hidden" value="([\w\.#]+)">'

    match = re.search(pattern, content)
    csrf_token = match.group(1)
    print 'csrf_token:', csrf_token

    data = {'csrf_token':csrf_token,'email':'172440249@qq.com', 'password':'luyasi'}
    jdata = json.dumps(data)
    loginRes = requests.post(loginurl, json=data, cookies=cookies)

    print loginRes.text

def test():
    toStr = "WyIxIiwiNjU0MGE0YjBiYzFhMjhlYTc2MzA4NmI5MzVkYmJkZjciXQ.CE__Tg.Y1DHCMk0STwrRpYUOkSmOaXBVMs"
    url= 'http://127.0.0.1:5000/api/blogs/3/?auth_token='+toStr
    res = requests.get(url)

    print res.text

test()