# -*- coding: utf-8 -*-
'''
@File  : xmind.py
@Author: 汪先锦
@Date  : 2020/5/21 15:41
@Desc  : 
'''
import xmind
xmind_file = 'docs/xmind_testcase_demo.xmind'
workbook = xmind.load(xmind_file)
data = workbook.getData()
print(data)


