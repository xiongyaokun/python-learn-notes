#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/18 10:05
# @Author  : xiongyaokun
# @Site    : 
# @File    : try-except-finally-example01.py
# @Software: PyCharm

print "Python 中 try, except, finally 的执行顺序。"
print "Test1"


# 在try中raise一个异常，就立刻转入except中执行，在except中遇到
# return时，就强制转到finally中执行，在finally中遇到return时就返回
def test1():
    try:
        print "to do stuff"
        raise Exception('hehe')
        # raise 下面的程序不会执行
        # print "to return in try"
        # return "try"
    except Exception:
        print "process except"
        print "to return in except"
        return "except"
    finally:
        print "to return in finally"
        return "finally"
test1Return = test1()
print "test1Return:", test1Return


#如果try中没有异常，就不会转到except中，在try中遇到return时，也会立即
# 强制转到finally中执行，并在finally中返回
def test2():
    try:
        print "to do stuff"
        print "to return in try"
        return "try"
    except Exception:
        print "process except"
        print "to return in except"
        return "except"
    finally:
        print "to return in finally"
        return "finally"
test2Return = test2()
print "test2Return:", test2Return

print "test1 和 test2 中得到的结论：无论是在try还是except中，遇到”\
      return时，只要设定了finally语句，就会中断当前的return语句，\
      跳转到finally中执行，如果finally中遇到return语句，就直接返回，\
      不再跳转try/except中被中断的return语句"


#test3 和 test4得到的结论：在except和try遇到return时，会锁定return
#的值，然后跳转到finally中，如果finally中没有return语句，则finally
#执行完毕之后仍返回原return点，将之前锁定的值返回（即finally中的动作不影响）
# 返回值，如果finally中有return语句，则执行finally中的return语句
def test3():
    i = 0
    try:
        i += 1
        print "i in try: %s" % i
        raise Exception("hehe")
    except Exception:
        i += 1
        print "i in except: %s" % i
        return i
    finally:
        i += 1
        print "i in finally: %s" % i
print "test3Return: %s" % test3()

def test4():
    i = 0
    try:
        i += 1
        return i
    finally:
        i += 1
        print "i in finally:%s" % i
print "test4Return:%s" % test4()


# test5() 在一个循环中，最终要跳出循环之前，会先转到finally执行，
# 执行完毕之后才开始下一轮循环
def test5():
    for i in range(5):
        try:
            print "do stuff %s" % i
            raise Exception(i)
        except Exception:
            print "exception %s" % i
            continue
        finally:
            print "do finally %s" % i
test5()