# -*- coding: utf-8 -*-
'''
@File  : mock_server.py
@Author: 汪先锦
@Date  : 2020/5/19 15:23
@Desc  : 
'''
from urllib import request

from  flask import Flask
import requests

app=Flask(__name__)

@app.route('/')
def hello():
    return "软件测试-自动化测试-性能测试-安全测试!"
#@app.route('/post',methods=['post'])
# def test_route():
#     d1=request.form['d1']
#     d2=request.form['d2']
#     return  d1+d2
if __name__ == '__main__':
    app.run("127.0.0.1","9090")