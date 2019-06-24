#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python 面向对象学习
@author: Yiwan
'''


# 面向对象技术简介
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 实例变量：定义在方法中的变量，只作用于当前实例的类。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 方法：类中定义的函数。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

# 创建类
# class ClassName:
#     '类的帮助信息'        #类文档字符串
#     class_suit          #类体

class Employee:
    '所有员工的基类'
    empCount = 0    #类变量，类的左右实例间共享
    
    def __init__(self,name,salary):     # 构造函数，初始化方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):     # self代表类的实例
        print "员工总数：%d", Employee.empCount
    
    def displayEmployee(self):
        print "姓名：%s, 薪资：%s" % (self.name,self.salary)

# self代表类的实例，而非类，类的方法和普通函数只有一个特别的区别——他们必须有一个额外的第一参数名称，通常都是self

class Test:
    def prt(self):          #self换成其他也可以正常执行
        print(self)
        print(self.__class__)
t = Test()      # 创建实例对象
t.prt

# 创建Employee类的第一个对象
emp1 = Employee('Zara',2000)
# 创建Employee类的第二个对象
emp2 = Employee('Manni',5000)

# 访问属性
emp1.displayEmployee()
emp2.displayEmployee()
print "总共总数：",Employee.empCount

# 添加，删除，修改类的属性
emp1.age  = 7   # 添加一个age属性
emp1.age = 8    # 修改age属性
del emp1.age    # 删除age属性

setattr(emp1, 'age', 8) # 添加属性age，值为8
hasattr(emp1, 'age') # 如果存在age属性就返回True
getattr(emp1, 'age') # 返回age属性的值
delattr(emp1, 'age')

# python内置属性
print "Employee.__doc__: ", Employee.__doc__
print "Employee.__name__: ", Employee.__name__
print "Employee.__module__: ", Employee.__module__
print "Employee.__bases__: ", Employee.__bases__
print "Employee.__dict__: ", Employee.__dict__

# Python 对象销毁
# 引用计数器和循环垃圾回收器
# 析构函数
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name,"销毁"
        
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3) # 打印对象的id
del pt1
del pt2
del pt3

# 类的继承
# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite

class Parent:       # 定义父类
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"
    def parentMethod(self):
        print "调用父类方法"
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        return self.parentAttr

# class Child(Parent):    # 定义子类
#     def __init__(self):
#         print "调用子类构造方法"
#     def childMethod(self):
#         print "调用子类方法"
#         
# c = Child()     # 实例化子类
# c.childMethod() # 调用子类的方法
# c.parentMethod()# 调用父类的方法
# c.setAttr(200)  # 再次调用父类的方法，设置属性
# c.getAttr()     # 再次调用父类的方法获取属性

# issubclass(),判断是不是子类
# isinstance(obj,Class)判断是不是一个类的实例化

# 方法的重写

# class Parent:        # 定义父类
#    def myMethod(self):
#       print '调用父类方法'
#  
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print '调用子类方法'
#  
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法

# 运算符重载

# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'Vector (%d,%d)' % (self.a,self.b)
#     def __add__(self,other):
#         return Vector(self.a+other.a,self.b+other.b)
# 
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print v1 + v2

# 双下划线开头为私有的
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
#  
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print self.__secretCount
#  
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.publicCount
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的
# print counter._JustCounter__secretCount

# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
