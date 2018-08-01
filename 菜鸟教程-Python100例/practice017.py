#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/10 10:42
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice017.py
# @Software: PyCharm

"""Q:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数."""
import re

s = raw_input("请输入任意字符串：-->")


# 方法一：
print "方法一："
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print "char = %d, space = %d, digit = %d, others = %d" % (letters, space, digit, others)



"""方法二："""
print "方法二："

r1 = re.compile('[a-zA-Z]')
r2 = re.compile('[0-9]')
print "英文字母的个数为：%d" % len(re.findall(r1, s))
print "数字的个数是：%d" % len(re.findall(r2, s))
print "空格的个数是：%d" % len(re.findall(' ', s))
print "其他字符的个数是：%d" % (len(s) - len(re.findall(r1,s)) - len(re.findall(r2,s)) -
                       len(re.findall(' ', s)))