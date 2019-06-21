#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time :    2019/6/20 下午11:27
@Author:  yiwanfeng
@File: sun_flower.py
@Software: PyCharm
@Mail: ily19910525fyw@126.com
@Description: 绘制太阳花
"""

import turtle as t
import time

t.color('red', 'yellow')
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)

t.end_fill()
time.sleep(60)

