#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 20:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice008.py
# @Software: PyCharm

"""Q:输出9×9乘法口诀表"""

def chengfakoujue():
    for i in range(10):
        for j in range(1, i+1):
            print '%d * %d = %2d   ' % (j, i, i*j) ,
        print
chengfakoujue()

print '**' * 30

def cf():
    for i in range(10):
        print
        for j in range(1, i+1):
            print "{} * {} = {}".format(j, i, j*i),

cf()