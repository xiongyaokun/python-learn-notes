#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/18 16:35
# @Author  : xiongyaokun
# @Site    : 
# @File    : print-format-out-example01.py
# @Software: PyCharm

'''
可以指定所需长度的字符串的对齐方式在；
< （默认）左对齐
>  右对齐
^  中间对齐
=  (只用于数字)在小数点后进行补齐
'''
print "1:\t|{0:>10}".format('xiongyaokun')
print "1:\t|{0:>10}".format('yaokun')
print "1:\t|{0:>5}".format('yaokun')

print "2:\t|{0:4.2f}".format(1.1415926)
print "2:\t\t|{0:4.2f}".format(1.1415926)

print "3:\t|", format(1.1416926,'<10.2f')
print "4:\t|{0:<10},{1:<15}".format('yaokun',1.1415926)
print "5:\t|User ID:{uid} Last seen: {last_login}".format(uid \
       ='root', last_login = '5 Mar 2008 07:20')


'''
格式化指示符可以包含一个展示类型来控制格式。
例如，浮点数可以被格式化为一般格式或用幂来表示。
'b' - 二进制。将数字以2为基数进行输出。
'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
'd' - 十进制整数。将数字以10为基数进行输出。
'o' - 八进制。将数字以8为基数进行输出。
'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
Python中格式化输出字符串使用format()函数, 字符串即类, 可以使用方法;
Python是完全面向对象的语言, 任何东西都是对象;
字符串的参数使用{NUM}进行表示,0, 表示第一个参数,1, 表示第二个参数, 以后顺次递加;
使用":", 指定代表元素需要的操作, 如":.3"小数点三位, ":8"占8个字符空间等;
'''
print "6:\t|{0:b}".format(3)
print "7:\t|{0:c}".format(3)
print "8:\t|{0:d}".format(3)
print "9:\t|{0:o}".format(3)
print "10:\t|{0:x}".format(3)
print "11:\t|{0:e}".format(3)
print "12:\t|{0:g}".format(3)
print "13:\t|{0:n}".format(3.75)
print "14:\t|{0:n}".format(3)
print "15:\t|{0:%}".format(3.75)

# 输入形式的控制
a = int(raw_input('a:'))
b = int(raw_input('b:'))
print "16:\t|%*.*f" % (a, b, 1.1415926)

print "17:\t|{array[2]}".format(array=range(10))
print "18:\t|{attr.__class__}".format(attr=0)
print "19:\t|{digit:*^ 10.5f}".format(digit=1.0/3)

'''
类和类型可以定义一个__format__()方法来控制怎样格式化自己。
它会接受一个格式化指示符作为参数：
'''
def __format__(self, format_spec):
    if isinstance(format_spec, unicode):
        return unicode(str(self))
    else:
        return str(self)
