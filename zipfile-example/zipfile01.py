#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/29 14:41
# @Author  : xiongyaokun
# @Site    : 
# @File    : zipfile01.py
# @Software: PyCharm

import zipfile, os

path = 'G:\\BaiduMusic\\Images\\'
zipName = path + 'BaiduMusic_Image.zip'

f = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print filename
        f.write(os.path.join(dirpath, filename))
f.close()
