#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time :    2019/6/20 下午11:03
@Author:  yiwanfeng
@File: first_demo.py
@Software: PyCharm
@Mail: ily19910525fyw@126.com
@Description: 直角螺旋线
"""
import turtle
import time
turtle.speed('fastest')
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)

