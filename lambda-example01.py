#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/18 14:18
# @Author  : xiongyaokun
# @Site    : 
# @File    : lambda-example01.py
# @Software: PyCharm


# lambda不会使代码运行效率提高，只是提高代码的简洁性
# lambda作为一个表达式，定义了一个匿名函数，x是入口参数，x+1 是函数体
g = lambda x: x + 1
print g(1) # 2
print g(2) # 3

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x:x % 3 == 0, foo)
print [x for x in foo if x % 3 == 0]

print map(lambda x: x * 2 + 10, foo)
print [x*2+10 for x in foo]

print reduce(lambda x, y: x + y, foo)


f1 = lambda x,y,z: x+y+z
print f1(1,2,3) # 6

f2 = lambda x,y=2,z=3: x+y+z
print f2(1,y=4,z=5) #10

# lambda 表达式常用来编写跳转表（jump table）,就是行为的列表或者字典
L = [
    (lambda x: x**2),
    (lambda x: x**3),
    (lambda x: x**4)
]
print L[0](2), L[1](2), L[2](2) # 4, 8, 16

D = {
    'f1': (lambda: 2+3),
    'f2': (lambda: 2*3),
    'f3': (lambda: 2**3)
}
print D['f1'](), D['f2'](), D['f3']()


# 列表解析比map解析更强大
print [x+y for x in range(5) if x%2 == 0 for y in range(10) if y%2 == 1]

for y in range(10):
    if y%2 == 1:
        print [x+y for x in range(5) if x%2 == 0]