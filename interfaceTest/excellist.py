# -*- coding: utf-8 -*-
'''
@File  : excellist.py
@Author: 汪先锦
@Date  : 2020/5/28 14:59
@Desc  :
'''

from xlrd import open_workbook
import os


def test_something(O2O):
    # 排除首行内容,把其他的用例写进数组里面
    cls = []  # 定义一个空列表
    filepath = os.path.join('D:\\softdate\\Workspac\\Auto\\data', 'O2O.xlsx')  # 获取路径,join拼接
    file = open_workbook(filepath)  # 打开这个excel
    sheet = file.sheet_by_name(O2O)  # 获取这个sheet
    nrow = sheet.nrows  # 读取行
    for i in range(nrow):  # 循环读取行
        if sheet.row_values(i)[0] != 'TEST':  # 过滤首行内容
            cls.append(sheet.row_values(i))  # 添加到 cls列表中
    print(cls)
    return cls


test_something(O2O='O2O')
