import unittest
from interfaceTest import HTMLTestRunner_cn
import os  # 系统方法
from interfaceTest import my_unittest as ut
import logging


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(ut.MyTestCase("test_train"))
    suit.addTest(ut.MyTestCase("test_caipiao"))
    suit.addTest(ut.MyTestCase("test_IP"))
    # suit.addTest(ut.MyTestCase("test_login"))
    path = 'D:\\softdate\\Workspac\\Auto\\Report\\'
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # else:
    #     pass
    report_path = path + 'index.html'
    report_title = u'自动化测试报告'
    desc = u'自动化测试报告详情'
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(fp, title=report_title, description=desc)
    runner.run(suit)
    logging.info('测试用例执行结束,报告已生成!')
