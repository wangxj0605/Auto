# -*- coding: utf-8 -*-
'''
@File  : FirstDemo.py
@Author: 汪先锦
@Date  : 2020/3/25 15:25
@Desc  : 
'''
from selenium import webdriver

driver = webdriver.Chrome("D:\softdate\Workspac\Auto\drivers\chromedriver.exe")
url = 'https:music.163.com'
driver.get(url)
from selenium import webdriver  # 导入webdriver包
from time import sleep
def login():
    pass
#    # driver = webdriver.Chrome('D:\softdate\Workspac\Auto\drivers\chromedriver.exe')  # 打开谷歌浏览器并命名为driver
#     # driver = webdriver.Firefox() #火狐浏览器
#     driver.maximize_window()  # 最大化浏览器（全屏）
#     driver.implicitly_wait(8)  # 设置隐式时间等待
#     driver.get('http://st.hub4.baozun.cn/login')  # 通过get()方法，打开一个url链接
#