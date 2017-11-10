#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作，删除操作
@author: Yiwan
'''

# 导包
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 获取游标
cursor = db.cursor()

# 编写SQL 语句
sql = "DELETE FROM employee WHERE AGE > %d" % (20)

try:
    # 执行数据库
    cursor.execute(sql)
    # 提交到数据库
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()