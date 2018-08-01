#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/1 11:49
# @Author  : xiongyaokun
# @Site    : 
# @File    : test02.py
# @Software: PyCharm

import time

try:
    try:
        f = file('test.txt')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            time.sleep(2)
            print line,
    except EOFError:
        print "\nWhy did you give me EOF?"
    finally:
        print "Cleaning up...closed the file."
        f.close()
except:
    print "Open an Error."