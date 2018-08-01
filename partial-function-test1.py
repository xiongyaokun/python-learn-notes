#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/25 18:08
# @Author  : xiongyaokun
# @Site    : 
# @File    : partial-function-test1.py
# @Software: PyCharm

import functools

def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    elif s1.lower() < s2.lower():
        return -1
    else:
        return 0

sorted_ignore_case = functools.partial(sorted, cmp=cmp_ignore_case)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])