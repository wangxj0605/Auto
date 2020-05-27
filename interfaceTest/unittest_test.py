import unittest
from interfaceTest import HTMLTestRunnerNew
import os  # 系统方法
from interfaceTest import my_unittest as ut

ABSPATH = os.path.realpath(os.path.dirname(__file__))
print(ABSPATH)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(ut.MyTestCase("test_train"))
    suit.addTest(ut.MyTestCase("test_caipiao"))
    suit.addTest(ut.MyTestCase("test_IP"))
    # suit.addTest(ut.MyTestCase("test_login"))
    path = 'D:/softdate/Workspac/Auto/Report/'
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # else:
    #     pass
    report_path = path + 'index.html'
    report_title = u'自动化测试报告'
    desc = u'自动化测试报告详情'
    fp = open(report_path, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(fp, title=report_title, description=desc)
    runner.run(suit)
    print("================测试结束,已经生成测试报告!=====================")
