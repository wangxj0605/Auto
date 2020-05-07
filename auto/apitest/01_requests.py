# -*- coding: utf-8 -*-
'''
@File  : 01_requests.py
@Author: 汪先锦
@Date  : 2020/4/28 17:04
@Desc  : 
'''
import unittest
import requests
url='https://selectcar.yiche.com/com/selectcarforapp?mid=7&s=4&page=1&pagesize=20&cityId=201'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        r=requests.get(url)
        print(r.text)
        print(r.headers)

if __name__ == '__main__':
    unittest.main()