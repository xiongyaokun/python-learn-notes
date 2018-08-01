#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/10 10:54
# @Author  : xiongyaokun
# @Site    : 
# @File    : eval-example01.py
# @Software: PyCharm

x = 1
y = 2
num = eval('x + y')
print 'num:', num

def g1():
    x = 2
    y = 3
    num1 = eval('x + y', globals())
    print 'num1:', num1
g1()

def g2():
    x = 2
    y = 3
    num2 = eval('x + y', locals())
    print 'num2:', num2
g2()

def g3():
    x = 2
    y = 3
    num3 = eval('x + y', globals(), locals())
    print 'num3:', num3
g3()