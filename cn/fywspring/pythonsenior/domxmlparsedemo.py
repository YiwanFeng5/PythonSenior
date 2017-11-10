#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python 中使用DOM来解析XML
@author: Yiwan
'''

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element: %s" % collection.getAttribute("shelf")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")
    mytype = movie.getElementsByTagName('type')[0]
    print "Type: %s" % mytype.childNodes[0].data
    myformat = movie.getElementsByTagName('format')[0]
    print "Format: %s" % myformat.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print "Description: %s" % description.childNodes[0].data
   