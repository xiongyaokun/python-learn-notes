#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/30 19:49
# @Author  : xiongyaokun
# @Site    : 
# @File    : test03.py
# @Software: PyCharm

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "(Initialized SchoolMember:%s)" % self.name

    def tell(self):
        '''Tell my details.'''
        print "Name:%s, Age: %s" % (self.name, self.age)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "(Initialized Teacher:%s)" % self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Salary:%d" % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "(Initialized Student:%s)" % self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Marks:%d" % self.marks

t = Teacher('Mrs.Shrividya', 40, 3000)
s = Student('Swaroop', 22, 75)

print '--'*25,'我是分割线', '--'*25

members = [t, s]
for member in members:
    # works for both Teachers and Students
    member.tell()