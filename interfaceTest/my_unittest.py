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
            'end': '北京',
            'ishigh': '1',
            'appkey': '6aab843350e75ae0'

        }
        r = requests.post('https://api.binstd.com/train/station2s', data=body, verify=False)
        print(r.text)
        status = r.json()
        self.assertEqual(status['status'], 0)

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
