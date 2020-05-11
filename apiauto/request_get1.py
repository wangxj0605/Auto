# -*- coding: utf-8 -*-
'''
@File  : request_get1.py
@Author: 汪先锦
@Date  : 2020/5/11 11:10
@Desc  : 
'''
import requests
'''
r.status_code #响应状态码 
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩 
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None 
r.json() #Requests 中内置的JSON 解码器 
r.url # 获取 url 
r.encoding # 编码格式 
r.cookies # 获取cookie 
r.raw #返回原始响应体 
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码 
r.raise_for_status() #失败请求(非200 响应)抛出异常 
r.content
'''

#请求博客首页
def get_无参():
    response=requests.get('http://www.cnblogs.com/yoyoketang/') #不带参数的
    print("响应代码是:",response.status_code)
    print(response.text)

def get_带参():
    par={'Keywords':'yoyoketang '}
    response=requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
    print("响应代码是:", response.status_code)
    print(response.text)





get_带参()