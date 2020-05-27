# -*- coding: utf-8 -*-
'''
@File  : 01_requests.py
@Author: 汪先锦
@Date  : 2020/4/28 17:04
@Desc  : 
'''
import unittest
import requests
url='https://selectcar.yiche.com/'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        payload={'mid':7,
                 's':4,
                 'page':1,
                 'pagesize':20,
        'cityId':20}
        r=requests.get(url,params=payload)
        print("返回信息是",r.text)
        #print("请求头是",r.headers)

if __name__ == '__main__':
    unittest.main()