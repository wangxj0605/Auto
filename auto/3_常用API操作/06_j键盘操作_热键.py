# -*- coding: utf-8 -*-
'''
@File  : 06_j键盘操作_热键.py
@Author: 汪先锦
@Date  : 2020-05-08 23:20
@Decs  :
'''
from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
driver.maximize_window()
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("自动化测试")
sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'a')
sleep(3)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'x')
sleep(3)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'v')
sleep(3)
driver.find_element_by_xpath('//input[@id="su"]').click()
sleep(3)
driver.quit()