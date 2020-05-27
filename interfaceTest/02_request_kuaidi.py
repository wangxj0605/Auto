# -*- coding: utf-8 -*-
'''
@File  : 02_request_kuaidi.py
@Author: 汪先锦
@Date  : 2020/5/13 15:10
@Desc  : 
'''
import requests

url = "http://www.kuaidi.com/index-ajaxselectinfo-4305442510173.html"

headers = {

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"

 } # get 方法其它加个 User-Agent 就可以了

s = requests.session()
print(s)
r = s.get(url, headers=headers,verify=False)

result = r.json()
print(r.text)


