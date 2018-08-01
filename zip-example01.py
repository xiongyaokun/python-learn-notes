#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 18:23
# @Author  : xiongyaokun
# @Site    : 
# @File    : zip-example01.py
# @Software: PyCharm


"""zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
利用*号操作符，可以将list unzip（解压）"""

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = [8, 9, 0, 1]

print [x] * 3
print zip(*[x]*3)

print zip(x,y,z)
print type(zip(x,y,z))

# unzip
print zip(*zip(x,y,z))


print '**'*30

# 实现矩阵的转至， 行列互换
a = [[1,2,3], [4,5,6], [7,8,9]]
print zip(*a)
print map(list, zip(*a))
