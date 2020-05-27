# -*- coding: utf-8 -*-
'''
@File  : mock_client.py
@Author: 汪先锦
@Date  : 2020/5/19 15:32
@Desc  : 
'''

import requests

# data={
#     'd1':'hello',
#     'd2':'falsk'
#
# }

rest=requests.get("http://127.0.0.1:9090")
#result=requests.post("http://127.0.0.1:9090/post",data=data)
print(rest.text)
#print(result.text)