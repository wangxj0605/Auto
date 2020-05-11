# -*- coding: utf-8 -*-
'''
@File  : 08_页面拖拽操作.py
@Author: 汪先锦
@Date  : 2020-05-11 22:23
@Decs  :
'''
from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
driver.maximize_window()