#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/30 15:41
# @Author  : xiongyaokun
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

class TransportTools:
    '''Represents transportation tools'''
    # 定义类的属性，此属性被类的所有实例共享
    commonTool = 'bus'
    def __init__(self, name):
        self.name = name

car = TransportTools('car')
print car.commonTool
print car.name

car.commonTool = 'train'

bike = TransportTools('bike')
print bike.commonTool
print bike.name