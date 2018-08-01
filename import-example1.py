#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/25 18:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : import-example1.py
# @Software: PyCharm

# try:
#     from json import dumps
# except ImportError:
#     from simplejson import dumps
# print dumps({'python': 2.7})


try:
    import json2
except ImportError:
    import simplejson as json
print json.dumps({'python': 2.7})