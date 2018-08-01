#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/9 17:15
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice014.py
# @Software: PyCharm

"""Q:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。"""

"""方法一："""
# n = int(raw_input("请输入一个正整数：".strip()))
# num = n
# list = []
# for a in range(2, num+1):
#     while num % a == 0:
#         list.append(str(a))
#         num = num / a
# # print list
# if len(list) == 1:
#     print "%d = 1 * %d" %(n, n)
# else:
#     print "%d =" % n, '*'.join(list)



"""方法二："""
x = int(raw_input("是否进入循环: (1/是，0/否) -->".strip()))

while x :
    n = int(raw_input("请输入一个整数：-->".strip()))
    print '%d =' % n,
    while n not in [1]:
        for a in range(2, n+1):
            if n % a == 0:
                n /= a
                if n == 1:
                    print '%d' % a
                else:
                    print '%d *' % a,
                break