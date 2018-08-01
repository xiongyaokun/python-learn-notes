#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/26 9:23
# @Author  : xiongyaokun
# @Site    : 
# @File    : old-new-class-example.py
# @Software: PyCharm


# old style class
class OldClass:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def hometown(self):
        print "My 'old' hometown is in AnHui province."

    def collage(self):
        print "I graduate from NCEPU_old."

# new style class
class NewClass(object):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def hometown(self):
        print "My 'new' hometown is in AnHui province."

    def collage(self):
        print "I graduate from NCEPU_new."

if __name__ == '__main__':
    oldStyle = OldClass('xiongyaokun', 28, 140)
    newStyle = NewClass('xiongyaokun', 28, 140)
    print type(oldStyle)
    print type(newStyle)

    # 函数dir 用于输出类所具有的属性
    print dir(oldStyle)
    print dir(newStyle)

    # 调用hometown方法
    oldStyle.hometown()
    newStyle.hometown()

    # 调用collage方法
    oldStyle.collage()
    newStyle.collage()