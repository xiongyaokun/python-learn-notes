#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 19:13
# @Author  : xiongyaokun
# @Site    : 
# @File    : example003.py
# @Software: PyCharm

"""Q:一个整数,它加上100后是一个完全平方数,在加上168又是一个完全平方数,求这个数是
多少?
"""
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n*n - 100
            print x


'''
分析：
设这个整数为x
1、 x+100=n^2和x+100+168=m^2
推出 m^2-n^2=168
即   （m+n)(m-n)=168
设    m+n=i m-n=j
则    i*j=168
由    i>0 j>0   推出  i%2=0 j%2=0
由    168=2*2*2*3*7
上面两个条件推出i与j值的范围[2,4,6,12,14,28,42,84]
反推：m=(i+j)/2和n=(i-j)/2 并且 n>0 推得 i>j
则     i=[14,28,42,84]
       j=[12,6,4,2]
'''
arr1 = [14, 28, 42, 84]
arr2 = [12, 6, 4, 2]
for i in range(0, 4):
    m1 = (arr1[i] + arr2[i]) / 2
    n1 = (arr1[i] - arr2[i]) / 2
    x = n1 * n1 - 100
    print x