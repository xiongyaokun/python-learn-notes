#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/3 4:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : test03.py
# @Software: PyCharm

import random


# stand = 36
stand = random.randint(1,100)
IN = raw_input("please input a int number: >>>")

result = True

while result:
    try:
        a = int(IN)
    except ValueError, e:
        print "catch error:", e
        IN = raw_input("please input an int number: >>>")

    else:
        if a == stand:
            result = False
            print "Congratulations, You get it!"
        elif a > stand:
            IN = raw_input("please input a smaller number: >>>")
        elif a < stand:
            IN = raw_input("please input a bigger number: >>>")
