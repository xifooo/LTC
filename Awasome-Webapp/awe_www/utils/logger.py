#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
import sys


# logger = logging.getLogger('my_logger')  # 创建一个logger对象
logger = logging.getLogger(__name__)  # 创建一个Logger对象，名称为模块的名称
logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

# 创建一个输出到标准输出（CLI）流的StreamHandler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

# 定义输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
console_handler.setFormatter(formatter)

# 将handler添加到logger对象中
logger.addHandler(console_handler)


# # 记录日志信息
# logger.info('Start application')
# logger.debug('Debug information')
# logger.warning('Warning information')
# logger.error('Error information')
# logger.critical('Critical information')

