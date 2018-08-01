#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/7 23:13
# @Author  : xiongyaokun
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

def dec(score):
    print "This is decorating start!"
    def exam():
        if score >= 60:
            print 'Passed'
        else:
            print 'Failed'
    return exam

ex = dec(90)
print type(ex)
ex()
