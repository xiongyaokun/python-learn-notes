#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/29 16:29
# @Author  : xiongyaokun
# @Site    : 
# @File    : zipfile-note02.py
# @Software: PyCharm

import zipfile

# 判断一个文件是否存在
zf = zipfile.ZipFile(r'D:\Python\learning-notes\zipfile-example\a byte of python.zip')
for filename in ['chapter9_01.py', 'test.txt']:
    try:
        info = zf.getinfo(filename)
    except KeyError:
        print 'ERROR: Did not find %s in zip file' % filename
    else:
        print "%s is %d bytes" % (info.filename, info.file_size)


# 从ZIP文档中提取文件
zf_1 = zipfile.ZipFile(r'D:\Python\learning-notes\zipfile-example\a byte of python.zip')
for filename in ['chapter9_01.py', 'test.txt']:
    try:
        data = zf.read(filename)
    except KeyError:
        print "ERROR: Did not find %s in zip file" % filename
    else:
        print filename
        print repr(data)
# 要提取的文件会被自动解压
zf.close()