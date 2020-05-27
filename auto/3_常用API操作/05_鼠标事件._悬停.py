# -*- coding: utf-8 -*-
'''
@File  : 05_鼠标事件.py
@Author: 汪先锦
@Date  : 2020-04-30 19:35
@Decs  :
'''

from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(3)
sleep(2)
qq=driver.find_elements_by_xpath('//*[@id="s_usersetting_top"]/span')
shoubiao=ActionChains(driver)
shoubiao.move_to_element(qq).perform()
sleep(2)
driver.close()
