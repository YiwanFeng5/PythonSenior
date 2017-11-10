#! /ur/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python数据库基本操作三，插入操作
@author: Yiwan
'''
# 导入MySQLdb包
import MySQLdb

# 获取数据库链接
db = MySQLdb.connect("127.0.0.1","root","root","testdb")

# 获得游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE VALUES("Mac","Mohan",20,'M',2000)"""
        
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果出现错误的话就回滚
    db.rollback()

# 关闭数据库
db.close()
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        