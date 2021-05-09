#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 9:43
# @Author  : Chocolate
# @Site    : 
# @File    : 爬取美篇图片.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os
import time
import js2xml
from lxml import etree
import random

url = 'http://www.baidu.com/link?url=0y0HQpNoALTsyOd0j-MsnEykrBtifZ5KoCsz3M-YWsc9q7ofOfCaZvVeZc-Hljv2'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'referer': 'https://www.meipian.cn/'
}
response = requests.get(url, headers=headers)  # 使用headers避免访问受限
soup = BeautifulSoup(response.content, 'lxml')
# 获取script里面的数据
script = soup.select("body script")[0].string
# 利用js2xml格式化script
script_text = js2xml.parse(script,encoding='utf-8',debug=False) # type <class 'lxml.etree._Element'>
script_tree = js2xml.pretty_print(script_text) # <class 'str'>
# etree只能解析Strings
seletor = etree.HTML(script_tree) # <class 'lxml.etree._Element'>
# 通过Xpath获取内容
img_urls = seletor.xpath('//property[@name="img_url"]/string/text()')

folder_path = 'D:/photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹


for img_url in img_urls:
    picture = requests.get(img_url)   # get函数获取图片链接地址，requests发送访问请求
    img_name = folder_path + str(random.sample('zyxwvutsrqponmlkjihgfedcba',10)) +'.jpg'
    with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
        file.write(picture.content)
        file.flush()
        file.close()  # 关闭文件
        time.sleep(1)  # 自定义延时
print('下载完成')

# for index,item in enumerate(items):
#     print(item)
#     if item:
#         html = requests.get(item.get('src'))   # get函数获取图片链接地址，requests发送访问请求
#         img_name = folder_path + str(index + 1) +'.jpg'
#         with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
#             file.write(html.content)
#             file.flush()
#         file.close()  # 关闭文件
#         print('第%d张图片下载完成' %(index+1))
#         time.sleep(1)  # 自定义延时
# print('抓取完成')