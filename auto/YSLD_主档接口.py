# -*- coding: utf-8 -*-
'''
@File  : YSLD_主档接口.py
@Author: 汪先锦
@Date  : 2020/4/14 14:09
@Desc  : 
'''
#如果需要登录，则通过下面方式认证(电脑的开机账号密码)，无需登录请忽略

from suds.transport.https import HttpAuthenticated
HttpAuthenticated(username='admin',passowrd='123')


    #如果不需要登录直接像下面这样
