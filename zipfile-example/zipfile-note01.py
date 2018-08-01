#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/29 14:48
# @Author  : xiongyaokun
# @Site    : 
# @File    : zipfile-note01.py
# @Software: PyCharm

import zipfile
import datetime

# 测试是否为ZIP文件
for filename in ['print_name.py', 'D:\\Python\\books\\a byte of python\\a byte of python.zip', 'uwsgi.zip', 'admin']:
    # 注意%20s 的用法，为了使输出对其
    # filename 目录得真实存在才可以，否则不会返回True
    # zipfile.is_zipfile(r'python.zip')  返回的是False
    print '%60s %s' %(filename, zipfile.is_zipfile(filename))

# 读取ZIP文件的内容
# 读取ZIP文件，返回文件名称的一个list
zf = zipfile.ZipFile(r'D:\Python\learning-notes\zipfile-example\a byte of python.zip', 'r')
print zf.namelist()

# 使用infolist()或者getinfo()可以从ZIP文件中获取更多信息：
def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print info.filename
        print '\tComment:\t', info.comment
        print '\tModified:\t', datetime.datetime(*info.date_time)
        print '\tSystem:\t\t', info.create_system,'(0=Windows, 3=Unix)'
        print '\tZIP version:\t', info.create_version
        print '\tCompressed:\t', info.compress_size,'bytes'
        print '\tUncompressed:\t', info.file_size,'bytes'
    zf.close()

if __name__ == '__main__':
    print_info(r'D:\Python\learning-notes\zipfile-example\a byte of python.zip')