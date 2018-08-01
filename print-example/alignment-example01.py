#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/29 19:42
# @Author  : xiongyaokun
# @Site    : 
# @File    : alignment-example01.py
# @Software: PyCharm

text = '我是字符串'

# 使用ljust() rjust() center()方法
print text
print text.ljust(20)
print text.rjust(20)
print text.center(20)
print text.ljust(20, '/')
print text.rjust(20, '~')
print text.center(20, '*')

# 使用format方法
print '--'*25, '我是分割线', '--'*25
print format(text, '>20'), '我是右对齐'
print format(text, '^20'), '我是居中对齐'
print format(text, '/<20'), '我是左对齐'
print format(text, '~>20'),
print format(text, '*^30')