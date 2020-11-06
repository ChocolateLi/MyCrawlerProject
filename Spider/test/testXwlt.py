#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 10:07
# @Author  : Chocolate
# @Site    : 
# @File    : testXwlt.py
# @Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象，相当于一个文件
worksheet = workbook.add_sheet('sheet1')    # 创建工作表
worksheet.write(0,0,'hello')    # 写入数据，第一个参数表示行，第二个参数表示列，第三个参数表示内容
workbook.save("student.xls")   # 保存数据表

