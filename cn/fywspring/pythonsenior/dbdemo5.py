#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作，更新操作
@author: Yiwan
'''

# 到数据库包
import MySQLdb

# 获取一个链接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 获取一个游标
cursor = db.cursor()

# 编写SQL
sql = "UPDATE employee SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print "插入成功"
except:
    # 发生错误时回滚
    print "出错啦"
    db.rollback()

# 关闭数据库连接
db.close()