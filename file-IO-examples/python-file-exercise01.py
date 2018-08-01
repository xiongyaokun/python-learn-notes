#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/12 12:04
# @Author  : xiongyaokun
# @Site    : 
# @File    : python-file-exercise01.py
# @Software: PyCharm

import configparser as cp

# cfg = cp.ConfigParser()
# cfg.read('imooc.txt')
# cfg.set('user_info', 'email', 'user@imoooc.com')
# print cfg.sections()

"""
ConfigParser和.ini文件的练习
"""

class Student_info(object):

    def __init__(self, record_file):
        self.logfile = record_file
        self.cfg = cp.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        se_list = self.cfg.sections()
        print '**'*15
        for se in se_list:
            print se
            print self.cfg.items(se)
        print '**'*15

    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    def delete_section(self, section):
        self.cfg.remove_section(section)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def save(self):
        fp = open('self.logfile', 'w')
        self.cfg.write(fp)
        fp.close()

# if "__name__" == "__main__":
info = Student_info('student_info.txt')
info.cfg_load()
info.cfg_dump()
info.set_item('user_info', 'pwd', 'abc')
info.cfg_dump()
info.add_section('login')
info.set_item('login', '2017-08-12', '20')
info.cfg_dump()
info.save()