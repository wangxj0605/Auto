import unittest
from selenium import webdriver
import os  # 系统方法
from interfaceTest import my_unittest as ut, HTMLTestRunner
from time import sleep


class MyTestCase(unittest.TestCase):
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


ABSPATH = os.path.realpath(os.path.dirname(__file__))
print(ABSPATH)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(ut.MyTestCase("test_login"))
    path = 'D:/softdate/Workspac/Auto/Report/'
    report_path = path + 'Hubindex.html'
    report_title = u'测试报告'
    desc = u'UI自动化测试报告详情'
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=report_title, description=desc)
    runner.run(suit)
