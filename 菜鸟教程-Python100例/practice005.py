#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 19:29
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice005.py
# @Software: PyCharm

"""Q:输入三个整数x,y,z，请把这三个数由小到大输出。"""

num = []
i = 0
while i < 3:
    # strip()方法用于移除字符串首尾指定的字符串（默认为空格）
    x = raw_input("请输入一个整数：".strip())
    num.append(int(x))
    i += 1
num.sort()
print num