#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/29 16:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : zipfile-note03.py
# @Software: PyCharm

import zipfile, datetime
# from zipfile_note01 import print_info
def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name,'r')
    for info in zf.infolist():
        print info.filename
        print '\tComment:\t', info.comment
        print '\tModified:\t', datetime.datetime(*info.date_time)
        print '\tSystem:\t\t', info.create_system,'(0=Windows, 3=Unix)'
        print '\tZIP version:\t', info.create_version
        print '\tCompressed:\t', info.compress_size,'bytes'
        print '\tUncompressed:\t', info.file_size,'bytes'
    zf.close()



# 创建一个新的ZIP文件
print "creating archive"
zf = zipfile.ZipFile(r'D:\Python\learning-notes\zipfile-example\a byte of python 01.zip','w')
try:
    print "adding text.txt"
    zf.write(r'D:\Python\learning-notes\zipfile-example\zipfile01.py')
finally:
    print "closing"
    zf.close()



print print_info(r'D:\Python\learning-notes\zipfile-example\a byte of python.zip')

print print_info(r'D:\Python\learning-notes\zipfile-example\a byte of python 01.zip')

# zf = zipfile.ZipFile(r'D:\Python\learning-notes\zipfile-example\a byte of python 01.zip','r')
# print zf.namelist()
# zf.close()