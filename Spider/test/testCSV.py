#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 19:33
# @Author  : Chocolate
# @Site    : 
# @File    : testCSV.py
# @Software: PyCharm

import csv

# CSV文件是一种类似与表格的文件

fp = open('test.csv','a+',newline="")
csv_fp = csv.writer(fp)  # 处理成支持CSV文件操作的对象（句柄）

# (1,2,3)
# [1,2,3]
# csv处理这些数据，一个逗号就相当于一个方框。csv逗号分隔值文件

my_list = ['python','哈哈哈','java']
# 写入数据。就是把一些用逗号分隔的数据写成一个表格
csv_fp.writerow(my_list)    # 表示写一行数据
fp.close()


