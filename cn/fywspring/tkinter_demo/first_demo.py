#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time :    2019/6/20 下午11:34
@Author:  yiwanfeng
@File: first_demo.py
@Software: PyCharm
@Mail: ily19910525fyw@126.com
@Description: 
"""

from tkinter import *

root = Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()



