#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 19:41
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice006.py
# @Software: PyCharm

"""Q:斐波那契数列"""
# a = 1
# b = 1
# i = 3

'''方法一：'''
# def fib(n):
#     a = 1
#     b = 1
#     i = 3
#     if n >= 2:
#         print '1'
#         print '1'
#         if n >3:
#             while i <= n:
#                 a, b = b, a+b
#                 print b
#                 i = i + 1
#
# n = raw_input("请输入一个大于2的整数:".strip())
# fib(int(n))

'''方法二：递归调用'''

# def fib_1(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib_1(n-1) + fib_1(n-2)
#
# print fib_1(10)

'''方法三：返回数组'''
def fib_2(n):
    f = [1, 1]
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n >= 3:
        for i in range(2, n):
            f.append(f[-1] + f[-2])
    return f
print fib_2(15)