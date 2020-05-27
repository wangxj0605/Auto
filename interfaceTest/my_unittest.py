import unittest
import requests
import json

from selenium import webdriver
from time import sleep

from interfaceTest import HTMLTestRunner


class MyTestCase(unittest.TestCase):
    def test_train(self):
        body = {
            'start': '上海',
            'end': '弋阳',
            'ishigh': '1',
            'appkey': '6aab843350e75ae0'

        }
        r = requests.post('https://api.binstd.com/train/station2s', data=body, verify=False)
        print(r.text)
        self.assertEqual(True, True)

    def test_caipiao(self):
        # headers = {'Content-Tpye': 'application/json'}
        url = 'https://api.binstd.com/caipiao/query'
        data = {
            'caipiaoid': '13',
            'issueno': '',
            'appkey': '6aab843350e75ae0'
        }
        r1 = requests.post(url, data)
        print(r1.text)

    def test_IP(self):
        body = {
            'ip': '192.168.40.131',
            'appkey': '6aab843350e75ae0'

        }
        r = requests.post('https://api.binstd.com/ip/location', data=body, verify=False)
        print(r.json())

    def test_login(self):
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
        self.assertEqual('HUB4接口平台', driver.title)
        driver.quit()

