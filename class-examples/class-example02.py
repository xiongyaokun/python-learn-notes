#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/27 9:03
# @Author  : xiongyaokun
# @Site    : 
# @File    : class-example02.py
# @Software: PyCharm

class Friends(object):

    def __init__(self, name, place, weight):
        self.name = name
        # '_'单下划线，定义类的私有属性，但是也是可以直接访问的
        self._place = place
        # '__'双下划线定义类的
        self.__weight = weight

    def return_name(self):
        return self.name
    def return_place(self):
        return self._place
    def return_weight(self):
        return self.__weight

friend = Friends('xiong', 'Beijing', '140')
# 直接调用方法
print friend.return_name()
print friend.return_place()
print friend.return_weight()
# 直接调用属性
print friend.name
print friend._place

print friend._Friends__weight

