# -*- coding: utf-8 -*-
'''
@File  : read_excel.py
@Author: 汪先锦
@Date  : 2020-05-27 22:25
@Decs  :
'''
import xlrd


def read_excel():
    ExcelFile = xlrd.open_workbook(r'D:\\softdate\\Workspac\\Auto\\data\\O2O.xlsx')
    sheet = ExcelFile.sheet_by_name('O2O')
    rows = sheet.row_values(0)  # 第三行
    cols = sheet.col_values(0)  # 第二列
    print(rows, cols)



read_excel()
