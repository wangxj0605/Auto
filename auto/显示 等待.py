# -*- coding: utf-8 -*-
'''
@File  : 显示 等待.py
@Author: 汪先锦
@Date  : 2020/4/13 17:06
@Desc  : 
'''

from  selenium  import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support  import expected_conditions as  EC

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
element.send_keys('selenium')
driver.quit()
