#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/25 23:41
# @Author  : xiongyaokun
# @Site    : 
# @File    : class-example-test1.py
# @Software: PyCharm

class Person(object):
    def __init__(self):
        self.name = None

    # pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
# L2 = sorted([p1.name, p2.name, p3.name])
# key 的参数用法
L2 = sorted(L1, key = lambda x: x.name)

print L2[0].name
print L2[1].name
print L2[2].name
# print sorted(L1, key=lambda x: x.name)
# print sort([L1[0].name, L1[1].name, L1[2].name])
# print sorted([p1.name, p2.name, p3.name])
# print sorted(L1)