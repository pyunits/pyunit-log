#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/23 17:15
# @Author: Jtyoui@qq.com
# 参考文档：https://docs.python.org/zh-cn/3.7/library/logging.handlers.html?highlight=timedrotatingfilehandler
from pyunit_log import Log, log
import logging


def test_custom_config():
    """测试自定义日志配置文件"""
    Log()
    # 加载默认配置文件，如果要自定义，流程如下：c = get_log_config() 先对c对象进行修改，set_log_file_config(c)

    logging.info('默认加载到root下')

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')


def test_log():
    """测试自动化日志"""

    @log('./logs')
    def division():
        s = 1 / 0
        return s

    division()


if __name__ == '__main__':
    test_custom_config()
    test_log()
