# -*- coding: utf-8 -*-
'''
@File  : utest.py
@Author: 汪先锦
@Date  : 2020/4/20 15:18
@Desc  : 
'''
import  unittest


# 定义继承自untitest.Testcase的测试类

class CalculaateTestCase(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(1+1,2,msg="断言1+1=2")

    def testSub(self):
        self.assertEqual(1-1,2,msg="断言1-1=0")
class UserTestCase(unittest.TestCase):
    def testUser(self):
        self.assertEqual("zhangshan","zhangshan",msg="断言1+1=2")

#创建一个测试加载器
loader=unittest.TestLoader()
#创建测试套件
suite=unittest.TestSuite()
#从测试类中加载测试用例
tests=loader.loadTestsFromTestCase(UserTestCase)
#将测试用例加载到测试组
suite.addTests(tests)
#创建测试运行器
with open("test_report,txt", "w")as f:
    runner=unittest.TextTestRunner(verbosity=2,stream=f)
    runner.run(suite)



# if __name__ == '__main__':
#     unittest.main()