#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作一,查看mysql版本
@author: Yiwan
'''
import MySQLdb

# 打开数据库链接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取一条数据
data = cursor.fetchone()
print "Database version: %s" % data

# 关闭数据库链接
db.close()







