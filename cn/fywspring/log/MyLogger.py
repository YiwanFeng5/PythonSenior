#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   PythonSenior
# File          :   MyLogger.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 16:19
# Software      :   PyCharm
# Description   :   简述
"""
import logging


class MyLogger(object):
    class MyLogger(object):
        def __init__(self):
            self.logfile = "/tmp/test.log"
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler(self.logfile)
            formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        def get_logger(self):
            return self.logger

    if __name__ == '__main__':
        my_logger = MyLogger().get_logger()
        my_logger.info("日志输出了")

