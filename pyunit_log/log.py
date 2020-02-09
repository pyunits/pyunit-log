#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/29 9:11
# @Author: Jtyoui@qq.com
import functools
import logging
import os
import logging.config
import configparser
import sys


class Log:
    """
    快速简单的函数日志模块，只需要在函数头上写一个装饰器即可，一行代码解决日志问题。\n
    @Log.log(log_file='./logs')
    """

    @staticmethod
    def set_log_config(config: configparser):
        """加载配置文件到内存"""
        logging.config.fileConfig(config)

    def get_log_config(self):
        """默认加载配置文件"""
        c = self.log_config()
        self.set_log_config(c)

    @staticmethod
    def log_config(config_path=None, log_save_dir=None) -> configparser:
        """加载当前文件下的log.ini文件

        默认日志文件夹在当前运训目录的logs下\n
        如果要自定义文件夹，只需要将custom_dir定义该目录即可，修改目录下的日志文件夹只需要定义handlers即可，程序会自动寻找handlers下的args的值。\n
        [handlers]\n
        keys = consoleHandler,fileHandler,errorHandler

        :param config_path: 日志配置文件
        :param log_save_dir: 自定义日志保存文件夹
        :return: 日志文件配置对象
        """
        cfg = configparser.RawConfigParser()
        if not config_path:
            config_path = os.path.dirname(__file__) + os.sep + 'log.ini'
        cfg.read(config_path)
        if log_save_dir:
            if not os.path.exists(log_save_dir):
                os.mkdir(log_save_dir)
            handle = cfg.items('handlers')
            for _, v in handle:
                for vs in v.split(','):
                    for key, value in cfg.items('handler_' + vs):
                        if key == 'args':
                            e = eval(value)
                            if isinstance(e[0], str):
                                es = log_save_dir + os.sep + os.path.basename(e[0])
                                value = str((es, *e[1:]))
                                cfg.set('handler_' + vs, 'args', value)
        else:
            if not os.path.exists('./logs'):
                os.mkdir('./logs')
        return cfg

    @classmethod
    def log(cls, log_file, config_file=None):
        """日志装饰器，用于测试函数的时候打印日志

        关于日志配置：可以参考官网配置： https://docs.python.org/3.7/library/logging.config.html

        :param log_file: 日志地址保存地方
        :param config_file: 日志配置地址保存地址
        """

        def inner(fun):
            cls.set_log_config(cls.log_config(config_path=config_file, log_save_dir=log_file))

            @functools.wraps(fun)
            def wraps(*args, **kwargs):
                try:
                    logging.getLogger('info').info(f'正在执行：{fun.__name__}函数')
                    f = fun(*args, **kwargs)
                    logging.getLogger('info').info(f'执行完毕：{fun.__name__}函数')
                    return f
                except Exception as e:
                    logging.getLogger('info').error(f'执行：{fun.__name__}函数异常，异常信息:{str(e)}')
                    with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                        f.write('+' * 70 + os.linesep)
                    logging.getLogger('error').exception(e)
                    with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                        f.write('#' * 70 + os.linesep + os.linesep)
                    raise e

            return wraps

        return inner
