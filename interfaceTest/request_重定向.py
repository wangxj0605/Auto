# -*- coding: utf-8 -*-
'''
@File  : request_重定向.py
@Author: 汪先锦
@Date  : 2020/5/13 15:32
@Desc  : 
'''
import requests

def login():
    url='http://test.account.baozun.cn/person/login'
    s=requests.session()

    data={
                'appkey':'IPWF-TEST',
                'password':'sZOL2h%2F2HbEAg5TVE%2BCN3Q%3D%3D',
                'loginName':'wangxianjin',
                'code':'',
                'domainLogin':'fasle',

    }
    response=s.post(url,data=data,headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SESSION=0b0e3019-f1e7-46b7-b582-09a5ca0a156b'},allow_redirects=True)
    # return response.text
    print(response.history)
if __name__ == '__main__':
    login()