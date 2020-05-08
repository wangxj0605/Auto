# -*- coding: utf-8 -*-
'''
@File  : 04_页面获取操作.py
@Author: 汪先锦
@Date  : 2020/4/30 15:48
@Desc  : 
'''
from selenium import webdriver
from  time import sleep

driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
temp=driver.find_element_by_xpath('//*[@id="bottom_layer"]/div[1]/p[2]/a')
print(temp.is_displayed()) #判断元素是否存在
print(temp.is_enabled())#是否可操作
print(temp.is_selected())#是否被选中
driver.quit()
