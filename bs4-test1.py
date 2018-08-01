#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/3 13:04
# @Author  : xiongyaokun
# @Site    : 
# @File    : bs4-test1.py
# @Software: PyCharm

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print (soup.prettify())
print 'soup.title = ', soup.title
print 'soup.title.name = ', soup.title.name
print 'soup.title.string = ', soup.title.string
print 'soup.title.parent.name = ', soup.title.parent.name
print 'soup.p = ', soup.p
print "soup.p['class'] = ", soup.p['class']
print 'soup.a = ', soup.a
print 'soup.fing_all("a") = ', soup.find_all('a')
print "soup.find(id = 'link3') = ", soup.find(id = 'link3')
# 从文档中找到所有<a>标签的连接：
print "从文档中找到所有<a>标签的连接："
for link in soup.find_all('a'):
    print link.get('href')
# 从文档中获取所有文字内容：
print '从文档中获取所有文字内容：'
print soup.get_text()
print 'type(soup.a) = ', type(soup.a)