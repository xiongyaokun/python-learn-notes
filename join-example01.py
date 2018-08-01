#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/27 1:04
# @Author  : xiongyaokun
# @Site    : 
# @File    : join-example01.py
# @Software: PyCharm

# Python中有join()和os.path.join()两个函数，具体作用如下：
# join():连接字符数组。将字符串、元组、列表中的元素以指定的字符（分隔符）连接生成一个新的字符串
# os.path.join(): 将多个路径组合后返回
import os

print "join()函数"
print "语法：'sep'.join(seq)"
print """
sep: separate 分隔符。可以为空
seq: sequence 要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
"""

# 对列表进行操作
seq1 = ['hello', 'good', 'boy', 'doiido']
print ' '.join(seq1)
print ':'.join(seq1)


# 对字符串进行操作
seq2 = "hello good boy doiido"
print ':'.join(seq2)

# 对元组进行操作
seq3 = ('hello', 'good', 'boy', 'doiido')
print ":".join(seq3)

# 对字典进行操作
seq4 = {'hello':1, 'good':2, 'boy':3, 'doiido':4}
print ':'.join(seq4)


path = os.path.join('hello/', 'you/', 'are/', 'welcome/')
print path

