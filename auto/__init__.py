# -*- coding: utf-8 -*-
'''
@File  : __init__.py.py
@Author: 汪先锦
@Date  : 2020/4/8 15:25
@Desc  : 
'''
import configparser
import codecs

class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self, filename):
        configpath = filename
        fd = open(configpath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):   #该方法返回的是项目路径
        return self.cf.get(env,name)


