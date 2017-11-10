#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python网络编程，服务端
@author: Yiwan
'''

import socket       # 导入 socket模块

s = socket.socket() # 创建scoet对象
host = socket.gethostname() # 获取本地主机名
port = 12345        # 设置端口

s.connect((host,port))
print s.recv(1024)
s.close()






