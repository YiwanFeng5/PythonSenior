#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time :    2019/6/20 下午11:10
@Author:  yiwanfeng
@File: colorful_line.py
@Software: PyCharm
@Mail: ily19910525fyw@126.com
@Description: 彩色螺旋线
"""

import turtle
import time
turtle.pensize(2)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'purple', 'blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
time.sleep(10)
