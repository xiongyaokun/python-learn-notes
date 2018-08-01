#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/1 10:23
# @Author  : xiongyaokun
# @Site    : 
# @File    : test01.py
# @Software: PyCharm


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input("Enter something --> ")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print "\nWhy did you give me a EOF?"
except ShortInputException, x:
    print "Your input length is %d, it is required at least %d" %(x.length, x.atleast)

# 如果没有异常的话，else 部分就会被执行
else:
    print "The 'else' is done!"
    print "No exception was raised!"

# 不管有没有异常，finally 部分都会被执行
finally:
    print "The finally is done!"