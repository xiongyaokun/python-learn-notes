#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/18 9:44
# @Author  : xiongyaokun
# @Site    : 
# @File    : try-except-example01.py
# @Software: PyCharm

# 方法一：捕获所有异常
# try:
#     a = b
#     b = d
# except Exception, e:
#     print Exception, ":", e

# 方法二：采用traceback模块查看异常
# import traceback
# try:
#     a = b
#     b = d
# except:
#     traceback.print_exc()

# 方法三：采用sys模块回溯异常
# import sys
# try:
#     a = b
#     b = d
# except:
#     info = sys.exc_info()
#     # print type(info)
#     # print info
#     print info[0], ":", info[1]

#方法四，把异常保存在文件中，分析异常
import traceback
try:
    a = b
    b = d
except:
    f = open("D:\Python\learning-notes\log.txt",'a')
    traceback.print_exc(file=f)
    # 一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。
    # flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。
    # 正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。
    # 至于close方法，原理是内部先调用flush方法来刷新缓冲区，再执行关闭操作，这样即使缓冲区数据未满也能保证数据的完整性。
    # 如果进程意外退出或正常退出时而未执行文件的close方法，缓冲区中的内容将会丢失。
    f.flush()
    f.close()