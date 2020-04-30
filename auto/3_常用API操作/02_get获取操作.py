# -*- coding: utf-8 -*-
'''
@File  : 02_get获取操作.py
@Author: 汪先锦
@Date  : 2020/4/28 11:29
@Desc  : 
'''
from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get(url='http:www.baidu.com')
time.sleep(1)
driver.maximize_window()
#driver.set_window_size(400,800)
#driver.find_element_by_xpath('//*[@id="u1"]/a[6]').click()
driver.find_element_by_xpath('//*[text()="贴吧"]').click()
# try:
#     assert 'laohu' in driver.page_source
# except Exception as e:
#     driver.get_screenshot_as_file('D:/QQ.png')  # 截图
# else:
    #print("用例执行成功!")
if '进入贴吧' in driver.page_source:
    print('用例执行成功!')
else:
    driver.get_screenshot_as_file('D:/wqtb.png')
    print("用例执行失败!")

driver.quit()
