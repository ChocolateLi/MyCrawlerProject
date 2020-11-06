#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 15:22
# @Author  : Chocolate
# @Site    : 
# @File    : testUrllib.py
# @Software: PyCharm

import urllib.request
import urllib.parse

# get方式请求
# response = urllib.request.urlopen("http://www.baidu.com")
response = urllib.request.urlopen("file:///D:/%E7%A0%94%E7%A9%B6%E5%AE%9E%E4%B9%A0/%E7%A0%94%E7%A9%B6%E7%94%9F%E5%AE%9E%E4%B9%A0%E5%B7%A5%E4%BD%9C%E4%BB%BB%E5%8A%A1%E6%8F%8F%E8%BF%B0/Contents2.html")
print(response.read())

# post方式请求   httpbin工具模拟
# data = bytes(urllib.parse.urlencode({'name':'chenli','age':'18'}),encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# 超时处理
# try:
#     response = urllib.request.urlopen("https://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except:
#     print("Time Out!")

# response = urllib.request.urlopen("http://www.douban.com")
# print(response.status)

# 模拟浏览器发送信息
# url = "https://httpbin.org/post"
# url = "https://www.douban.com/post"
# data = bytes(urllib.parse.urlencode({'name':'chenli','age':'18'}),encoding="utf-8")
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
# }
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# 模拟浏览器向豆瓣发信息
# url = "https://www.douban.com"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
# }
# req = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))