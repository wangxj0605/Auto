# -*- coding: utf-8 -*-
'''
@File  : request_jenkins.py
@Author: 汪先锦
@Date  : 2020/5/11 13:39
@Desc  : 
'''
import requests
import re
import json
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

def jenkins():

    url= "http://localhost:8080/jenkins/j_acegi_security_check"
    header={'ser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            }
    body=d = {"from": "",

             "j_password": "wang@123",

             "j_username": "admin",

             "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1",

             "json": {"j_username": "wagnxixanjin",

             "j_password": "wang@123",

             "remember_me": True,

             "from": "",

             "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1"},

            "remember_me": "on",

             "Submit": u"登录"

 }
    #body=json.dumps(body)
    response=requests.post(url,data=body,headers=header)
    t = re.findall(r'<b>(.+?)</b>', response.text)
    print(t)

    print(response.text)
jenkins()
def https():


   # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    url = "https://passport.cnblogs.com/user/signin"

    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"

    }

    r = requests.get(url, headers=headers, verify=False)

    print(r.status_code)
if __name__ == '__main__':
    https()