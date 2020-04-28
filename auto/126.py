# -*- coding: utf-8 -*-
'''
@File  : 126.py
@Author: 汪先锦
@Date  : 2020/4/10 15:57
@Desc  : 
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.126.com/')
driver.maximize_window()
print('Before login================================>>')
#打印当前页的title
print(driver.title)
#打印当前页的URL
print('当前页面的Url是：%s'%driver.current_url)
driver.find_element_by_id('switchAccountLogin').click()
print('点击密码登录')
#driver.implicitly_wait(8)
#driver.find_element_by_name('email-box').clear()
driver.implicitly_wait(8)
driver.find_element_by_xpath('//input[@name="email" and @data-type="email"]').send_keys('wangxj0605')
print('输入账号')
#driver.implicitly_wait(8)
#driver.find_element_by_name('password').clear()
driver.implicitly_wait(8)
driver.find_element_by_name('password').send_keys('wang@123')
driver.implicitly_wait(8)
driver.find_element_by_id('dologin').click()




driver.quit()