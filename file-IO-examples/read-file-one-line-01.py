#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/28 11:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : read-file-one-line-01.py
# @Software: PyCharm

f= open('test01.txt')
# 一次全部读取
# print f.read()
# 读取单行
print f.readline()
# 读取指定的长度的字符
print f.readline(20)
f.close()

num = 0

with open('test01.txt') as f:
    for line in f:
        num += 1
        if  3 < num <6:
            print line
    f.close()
