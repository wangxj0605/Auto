# -*- coding: utf-8 -*-
'''
@File  : RUN.py
@Author: 汪先锦
@Date  : 2020/4/20 15:42
@Desc  : 
'''

import unittest


#创建一个测试加载器
loader=unittest.TestLoader()
#创建测试套件
suite=unittest.TestSuite()
#从测试类中加载测试用例
tests=loader.loadTestsFromTestCase(UserTestCase)
#将测试用例加载到测试组
suite.addTest(tests)
