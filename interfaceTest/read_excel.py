# -*- coding: utf-8 -*-
'''
@File  : read_excel.py
@Author: 汪先锦
@Date  : 2020-05-27 22:25
@Decs  :
'''
import xlrd

def read_excel():

    ExcelFile=xlrd.open_workbook(r'E:\\workSpace\\Auto\\data\\CORD E2E性能测试数据准备.xlsx')
    sheet =ExcelFile.sheet_by_name('门店SKU信息')
    rows=sheet.row_values(2) #第三行
    cols=sheet.col_values(1)#第二列
    print(rows,cols)
read_excel()