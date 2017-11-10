#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作二，创建表employee
@author: Yiwan
'''
import MySQLdb

# 打开数据库链接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# 如果数据表已经存在使用execute()方法删除表
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)"""
cursor.execute(sql)
# 关闭数据库链接
db.close()







