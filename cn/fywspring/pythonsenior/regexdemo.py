#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python中正则的使用，re模块
@author: Yiwan
'''

# re.match(pattern,string,flags=0)
# 参数    描述
# pattern    匹配的正则表达式
# string    要匹配的字符串。
# flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功re.match方法返回一个匹配的对象，否则返回None。
# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
# 匹配对象方法    描述
# group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

# 实例1
import re
from re import match
print (re.match('www', 'www.baidu.com')) # 不在起始位置匹配

# 实例2
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print "捕获组1：", matchObj.group()
    print "捕获组2：", matchObj.group(1)
    print "捕获组3：", matchObj.group(2)
else:
    print "没有匹配到"

# re.search(pattern,string,flags=0)
# 扫描整个字符串并返回第一个成功的匹配

print (re.search('www', 'www.baidu.com'))
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print "捕获组1：", searchObj.group()
    print "捕获组1：", searchObj.group(1)
    print "捕获组1：", searchObj.group(2)

# re.match和re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

# 检索和替换re.sub
# re.sub(pattern, repl, string, count=0, flags=0)
# 参数：
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = '2004-959-559 # 这是一个国外电话号码'

# 删除字符串中的Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是：",num

# 删除非数字（-）的字符
num = re.sub(r'\D', "", phone)
print "电话号码是：", num

# repl参数是函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print (re.sub('(?P<value>)\d+', double, s))

# 正则表达式修饰符 - 可选标志

# 修饰符    描述
# re.I    使匹配对大小写不敏感
# re.L    做本地化识别（locale-aware）匹配
# re.M    多行匹配，影响 ^ 和 $
# re.S    使 . 匹配包括换行在内的所有字符
# re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

# 特殊字符类
# 实例    描述
# .    匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d    匹配一个数字字符。等价于 [0-9]。
# \D    匹配一个非数字字符。等价于 [^0-9]。
# \s    匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S    匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w    匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W    匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。














