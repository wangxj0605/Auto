# -*- coding: utf-8 -*-
'''
@File  : 08_多窗口句柄操作.py
@Author: 汪先锦
@Date  : 2020-05-11 19:50
@Decs  :
'''
from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'t')
driver.execute_script("window.open('http://www.baidu.com/')")#弹出新窗口
hands=driver.window_handles
driver.switch_to.window(hands[1])
sleep(2)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys('haha')
driver.quit()