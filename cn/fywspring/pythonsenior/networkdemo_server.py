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
s.bind((host,port)) # 绑定端口

s.listen(5)         # 等待客户端连接
while True:
    c,addr = s.accept() # 建立客户端连接
    print '连接地址：', addr
    c.send('欢迎访问本服务器……')
    c.close()       #关闭连接






