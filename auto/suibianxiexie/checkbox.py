# -*- coding: utf-8 -*-
'''
@File  : checkbox.py
@Author: 汪先锦
@Date  : 2020/4/14 16:50
@Desc  : 
'''
import os,time
from selenium import  webdriver

driver=webdriver.Chrome()
driver.get(url='')
inputs=driver.find_elements_by_tag_name('input')


for  i  in inputs:
    if i.get_attribute('type')=='checkbo':
        i.click()
        time.sleep(1)
driver.quit()

