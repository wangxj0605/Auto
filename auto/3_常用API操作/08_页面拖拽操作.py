# -*- coding: utf-8 -*-
'''
@File  : 08_页面拖拽操作.py
@Author: 汪先锦
@Date  : 2020-05-11 22:23
@Decs  :
'''
from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('https://news.baidu.com')
driver.maximize_window()
ActionChains=ActionChains(driver)
#第一种拖拽方法(精准)
# target_elem1=driver.find_element_by_xpath('//*[@id="city_name"]/a')
# driver.execute_script("return arguments[0].scrollIntoView();",target_elem1)
#第二种页面拖拽方法(通过做标,不精准)
driver.execute_script("scroll(0,5000)")
sleep(4)
driver.quit()
