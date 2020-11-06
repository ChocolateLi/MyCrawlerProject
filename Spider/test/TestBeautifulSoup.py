#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 20:09
# @Author  : Chocolate
# @Site    : 
# @File    : TestBeautifulSoup.py
# @Software: PyCharm

"""
BeautifulSoup4把复杂的HTML转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：
-Tag    标签及其内容，默认拿到第一个出现的内容
-NavigableString    标签里的内容（字符串） （常用）
-BeautifulSoup  表示整个文档  （常用）
-Comment    是一个特殊的NavigableString，输出的内容不包含注释符号  （了解）
"""

from bs4 import BeautifulSoup
import re

# 读取当前目录的网页内容
file = open("./Contents2.html","rb")
html = file.read()
# 解析html网页
bs = BeautifulSoup(html,"html.parser")

# --------------了解内容----------------
# print(bs.title) # 包括标签和内容
# print(bs.title.string) # 只有内容
# print(bs.head)
#print(type(bs.title)) # 类型：<class 'bs4.element.Tag'>
# print(type(bs.title.string)) # 类型：<class 'bs4.element.NavigableString'>
# print(bs.table.attrs) # 拿到标签里的属性值
# print(type(bs)) # 类型：<class 'bs4.BeautifulSoup'>
# print(bs) # 整个文档，一个树形结构

# --------------应用部分-----------------
# 文档的遍历
# print(bs.head.contents) # 文档内容列表
# print(bs.head.contents[1])
# 这一部分不太常用到，用的更多的是文档的搜索。这部分用到时，可以去查找BeautifulSoup文档


# 文档的搜索
# 一、
# (1) find_all()查找所有
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("td")
# print(t_list)

# search()
# 正则表达式搜索 re是正则表达的包
# t_list = bs.find_all(re.compile("td"))
# print(t_list)

# 方法：自己定义一个方法（函数）,根据函数的规则来进行搜索 (功能很强大，了解）
# def name_is_exists(tag):
#     # 表示拥有属性name的都搜出来
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# print(t_list)

# (2)kwargs 参数
# t_list = bs.find_all(content="zh-ch ")
# for item in t_list:
#     print(item)

# (3)text参数
# t_list = bs.find_all(text="微信")
# t_list = bs.find_all(text=re.compile("\d")) # 跟正则表达式配合使用
# for item in t_list:
#     print(item)

# (4)limit参数
# t_list = bs.find_all("td",limit=3)
# for item in t_list:
#     print(item)

# 二、css选择器来查找
# select()
t_list = bs.select("td")
# for item in t_list:
#     print(item)
print(type(t_list))



