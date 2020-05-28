# -*- coding: utf-8 -*-
'''
@File  : logg.py
@Author: 汪先锦
@Date  : 2020-05-27 20:24
@Decs  :
'''
import logging
import os.path

path = 'D:\\softdate\\Workspac'


class log():
    def __init__(self):
        # 第一步 创建第一个logger,打开Log等级总开关
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 第二步,创建一个handler,用于写入日志文件 -Handler 处理器,将(记录器产生的)日志记录发送至适合的目的地
        handler = logging.FileHandler(path + '\\Auto\\log\\unittest.log', encoding='utf-8')
        # 第三步 定义handler的输出格式,Frommatter格式化器,指明了最终输出中日志记录的布局
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 使用formatter对象设置日志信息最后的规则,结构和内容,默认时间格式为:%Y-%m-%d %H:%M:%S
        handler.setFormatter(formatter)
        # 第四步 将logger添加到handler里面,为Logger实例增加一个处理器
        self.logger.addHandler(handler)

        # 第五步 创建一个调用方法

    def get_logger(self, message):
        self.logger.info(message)
