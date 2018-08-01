#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/18 15:26
# @Author  : xiongyaokun
# @Site    : 
# @File    : Fibonacci-example.py
# @Software: PyCharm

# 方法一， 直接打印出数列
def Fibonacci(param):
    n, a, b = 0, 0, 1
    while n < param:
        print b
        a, b = b, a+b
        n = n+1
print Fibonacci(5)

# 返回一个list
def Fib_1(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a+b
        n = n+1
    return L
print Fib_1(6)

# generator函数
def Fib_02(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

for n in Fib_02(5):
    print n

F = Fib_02(3)
print F.next()
print F.next()
print F.next()
print F.next()
print F.next()