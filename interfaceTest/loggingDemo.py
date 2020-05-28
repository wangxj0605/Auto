# -*- coding: utf-8 -*-
'''
@File  : loggingDemo.py
@Author: 汪先锦
@Date  : 2020/5/27 15:52
@Desc  : 
'''

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='D:\softdate\Workspac\Auto\log\myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
# 设置格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
# 告诉handler使用这个格式
console.setFormatter(formatter)
# add the handler to the root logger
# 为root logger添加handler
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
# 默认使用的是root logger
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
