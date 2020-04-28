# -*- coding: utf-8 -*-
'''
@File  : httpquest.py
@Author: 汪先锦
@Date  : 2020/4/18 13:19
@Desc  : 
'''
import requests

url='http://uatadmin.shopdog.com.cn/deli/test/add'
data={'brandCode':'NIKE','channelCode':'1Nike官方旗舰店','skus':'488371-200-9=1','type':'1','pgMode':'1','count':'1','platType':'31','sourceSys':'NDOMS','storeCode':'3670','paymentTime':'2020-04-15 00:00:00'}
res=requests.post(url,data)
print(res.text)