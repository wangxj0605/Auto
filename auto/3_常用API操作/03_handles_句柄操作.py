# -*- coding: utf-8 -*-
'''
@File  : 03_handles_句柄操作.py
@Author: 汪先锦
@Date  : 2020/4/30 14:13
@Desc  : 
'''
from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get(url='http://news.baidu.com/')
time.sleep(1)
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[text()="全面小康：一个都不能少"]').click()
time.sleep(5)
print(driver.title)
print(driver.window_handles) #获取所有的句柄
hand=driver.window_handles
print(driver.current_window_handle)#获取所有的句柄
driver.switch_to.window(hand[-1])
print("当前的title是:"+driver.title)
time.sleep(2)
print("当前的句柄是:"+driver.current_window_handle
)
driver.quit()
