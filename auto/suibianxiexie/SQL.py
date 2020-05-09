# -*- coding: utf-8 -*-
'''
@File  : SQL.py
@Author: 汪先锦
@Date  : 2020/5/7 15:54
@Desc  : 
'''
import pymysql
from selenium import webdriver
import time
def testui():
    driver = webdriver.Chrome()
    driver.get("http://www.sogou.com")
    #获取当前浏览器在屏幕上的位置，返回的是字典对象
    position=driver.get_window_position()
    print("当前浏览器所在位置的横坐标：",position['x'])
    print("当前浏览器所在位置的纵坐标：",position['y'])
    #设置当前浏览器在屏幕上的位置
    driver.set_window_position(y=200, x=400)
    print(driver.get_window_position())
    driver.close()

def readSQL():
    # 查询SQL语句
    sql = "SELECT * from t_shop_info where contact_code='BD-N-CONVERSE';"
    # 打开MySQL数据库连接
    coon = pymysql.connect(user='u_hub3_test', passwd='root1234', db='db_hub3_test', port=3306, host='10.88.26.36', charset='utf8')
    # 获取数据库操作游标
    cursor = coon.cursor()
    # 执行MySQL查询语句
    aa = cursor.execute(sql)
    # 获取执行查询语句后的结果数据列表
    info = cursor.fetchmany(aa)
    print(info)
    # 提交
    coon.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    coon.close()


if __name__ == '__main__':
    testui()


