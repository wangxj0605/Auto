# -*- coding: utf-8 -*-
'''
@File  : 松勤签到.py
@Author: 汪先锦
@Date  : 2020/4/9 14:55
@Desc  : 
'''
import random
from time import sleep

from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

url='http://vip.ytesting.com/loginController.do?login2'
d=webdriver.Chrome()
d.maximize_window()
d.get(url=url)

#d.find_element_by_id('userName').send_keys(Keys.BACK_SPACE)


d.find_element_by_id('password').send_keys('549382777')

lf=d.find_element_by_id('nc_1_n1z')

rf=d.find_element_by_class_name('nc-lang-cnt')
ActionChains(d).drag_and_drop_by_offset(lf, int(365.03) , 32).perform()
d.implicitly_wait(10)
ActionChains(d).move_to_element(lf).release()
sleep(1)
d.find_element_by_id('but_login').click()
sleep(10)
d.quit()


