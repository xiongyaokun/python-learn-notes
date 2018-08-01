#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 16:18
# @Author  : xiongyaokun
# @Site    : 
# @File    : example001.py
# @Software: PyCharm

"""Q:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""

'''Answer 1'''
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != j) and (i != k) and (j != k):
#                 print i,j,k

'''Answer 2'''
num = range(1,5)
# for i in num:
#     for j in num:
#         for k in num:
#             if i != j != k:
#                 print i,j,k

'''Answer 3'''
for i in num:
    for j in num:
        for k in num:
            l = [i,j,k]
            if len(set(l)) == 3:
                print i,j,k



'''Answer 4'''
# from itertools import permutations
# for i in permutations([1, 2, 3, 4], 3):
#     print i