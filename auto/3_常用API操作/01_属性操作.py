# -*- coding: utf-8 -*-
'''
@File  : 属性操作.py
@Author: 汪先锦
@Date  : 2020/4/28 11:11
@Desc  : 
'''
from selenium import webdriver
from time import sleep


def testBaidu():
    liulanqi = ['chrome', 'Ie', 'firefox']
    driver = webdriver.Chrome()  # 设置谷歌浏览器s
    driver.get("http://www.baidu.com")  # 请求地址
    driver.implicitly_wait(20)
    # driver.maximize_window()  # 浏览器最大化
    driver.set_window_size(400, 800)
    driver.find_element_by_id("kw").send_keys("软件自动化测试")
    driver.find_element_by_id("su").click()
    driver.implicitly_wait(10)
    print(driver.session_id)  # 打印session_id
    print(driver.name)  # 打印出浏览器名称
    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.get('http://test.account.baozun.cn/person/login?appkey=IPWF-TEST')
    sleep(2)
    driver.find_element_by_id("loginid").send_keys('wangxianjin')
    sleep(2)
    driver.find_element_by_id("userpassword").send_keys('wang@123')
    sleep(2)
    driver.find_element_by_id("login").click()
    sleep(2)

    print(driver.title)

    driver.quit()


if __name__ == '__main__':
    test_login()
