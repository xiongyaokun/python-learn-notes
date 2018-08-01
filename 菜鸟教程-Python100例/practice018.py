#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/10 11:00
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice018.py
# @Software: PyCharm


"""
Q:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加由键盘控制。
"""

print "方法一："
a = raw_input("请输入一个数字：-->")
b = int(raw_input("请输入一个数字(0~9)：-->"))
sum = 0
s = ''
for i in range(1, b+1):
    sum += int(a*i)
    if i != b :
        s = s + a*i + "+"
    else:
        s = s + a*i
print "%d = %s" % (sum, s)
