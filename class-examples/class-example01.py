#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/26 10:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : class-example01.py
# @Software: PyCharm

class lover(object):

    def __init__(self, name, place, time, begin_reason, end_reason):
        self.name = name
        self.place = place
        self.time = time
        self.begin_reason = begin_reason
        self.end_reason = end_reason

    def how_begin(self):
        print "I met %s in %s %s %s." % (self.name, self.time, self.place, self.begin_reason)

    def why_end(self):
        print "I left you, because %s." % self.end_reason

my_lover = lover('you', 'somewhere', 'future', 'by accident', 'the further away I am, the happier you will be')
print my_lover.how_begin()
print my_lover.why_end()