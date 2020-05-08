# -*- coding: utf-8 -*-
'''
@File  : 06_键盘操作.py
@Author: 汪先锦
@Date  : 2020-05-08 23:11
@Decs  :
'''
from selenium import webdriver
from  time import sleep
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
list = ['呵呵','哈哈','测试']
driver.maximize_window()
for i in list:
    driver.find_element_by_xpath('//input[@id="kw"]').clear()
    sleep(1)
    driver.find_element_by_xpath('//input[@id="kw"]').send_keys(i)
    sleep(1)
    driver.find_element_by_xpath('//input[@id="su"]').click()
driver.quit()
