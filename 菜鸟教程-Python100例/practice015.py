#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/10 9:56
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice015.py
# @Software: PyCharm

"""
Q:利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示.
"""

score = int(raw_input("请输入一个分数：-->".strip()))

# 方法一：
# if 0<= score <60:
#     print "Your level is C."
# elif 60 <= score <= 89:
#     print "Your level is B."
# elif 90 <= score <=100:
#     print "Your level is A."
# else:
#     print "Please input a number between 0 and 100."


# 方法二：
print (['C', 'C', 'B', 'A'][score/30])