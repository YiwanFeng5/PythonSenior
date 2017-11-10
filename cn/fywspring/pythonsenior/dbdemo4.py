#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作四，查询操作
@author: Yiwan
'''
import MySQLdb

# 获取链接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 获取游标
cursor = db.cursor()

# 编写SQL语句
sql = "SELECT * FROM employee WHERE INCOME > %d" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 遍历结果集results
    for result in results:
        fname = result[0]
        lname = result[1]
        age = result[2]
        sex = result[3]
        incom = result[4]
        print "名：%s, 姓：%s, 年龄：%d, 性别：%s, 收入：%d" % (fname,lname,age,sex,incom)
except:
    print "没有查到数据！"
    
# 关闭数据库
db.close()