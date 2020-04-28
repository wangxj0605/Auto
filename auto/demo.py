# -*- coding: utf-8 -*-
'''
@File  : demo.py
@Author: 汪先锦
@Date  : 2020/4/8 15:25
@Desc  : 
'''
from selenium import webdriver
driver = webdriver.Chrome("D:\softdate\Workspac\Auto\chromedriver.exe")
driver.get('http:/www.baidu.com')
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.find_element_by_id('loginid').send_keys('WSH10112')
# driver.find_element_by_id('userpassword').send_keys('wxj@0605')
# driver.implicitly_wait(3)
# driver.find_element_by_id('login').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/a[2]/li/span').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[3]/div[2]/div[3]').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[1]/label').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[2]/div[1]/div[1]').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[4]').click()
size=driver.find_element_by_id('kw').size
print(size)
text=driver.find_element_by_id("bottom_layer").text
print(text)
attribute=driver.find_element_by_id('kw').get_attribute('type')
print(attribute)
resule=driver.find_element_by_id('kw').is_displayed()
print("元素是否可见：%s"%resule)
driver.quit()