# -*- coding: utf-8 -*-
'''
@File  : 05_鼠标事件_右击.py
@Author: 汪先锦
@Date  : 2020-05-08 22:57
@Decs  :
'''

from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('http:www.baidu.com')
driver.maximize_window()
element=driver.find_elements_by_xpath('.//*[@id="lg"]/img[1]')
actionChains=ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
sleep(2)
driver.quit()