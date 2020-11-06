#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 10:00
# @Author  : Chocolate
# @Site    : 
# @File    : MySpider.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re
import csv

# findTr = re.compile(r'<tr></tr>')
# 找到td的内容的正则表达式
findTd = re.compile(r'<td>(.*)</td>')


def main():
    # 1、爬取网页数据（即获取网页数据）
    # 2、解析网页数据
    data = getData()
    # 3、继续处理数据
    data2 = dealData(data)
    # 4、弥补缺失数据。少了两个app的安装路径
    missingData(data2[0])
    # 5、再一次处理数据
    data3 = dealData2(data2)
    # 6、最后处理数据
    LastData = dealDataLast(data3)
    # 7、保存数据
    savaData(LastData)



# 1、获取网页数据并解析数据
def getData():
    file = open("Contents2.html", 'rb')  # 打开文件
    html = file.read()
    # # 2、解析网页数据
    soup = BeautifulSoup(html, "html.parser")  # 解析html网页

    # print(soup)
    # 一个tabled对应我们需要的一个列表信息,然后在列表中继续寻找我们需要的信息
    data = []
    for item in soup.find_all("table", class_="OuterTable"):
        item = str(item)  # 转成字符串方便处理
        # print(len(item))
        td = re.findall(findTd, item)
        # print(td)
        data.append(td)
    # print(data)
    return data


def dealData(data):
    data2 = []
    for item in data[0:4:]:
        item = item[3:]
        data2.append(item)
    for item in data[4:6]:
        item = item[2:]
        data2.append(item)
    for item in data[6:7:]:
        item = item[4:]
        data2.append(item)
    for item in data[7:8]:
        item = item[7:]
        data2.append(item)
    for item in data[8:]:
        item = item[8:]
        data2.append(item)
    # for item in data2:
    #      print(item)
    return data2


def missingData(data):
    data.insert(31, "/private/var/containers/Bundle/Application/453C6FC0-DE97-4182-9D55-795A348EF8B8/QQ.app")
    data.insert(49, "/private/var/containers/Bundle/Application/28D3C183-D832-4923-9E53-8CB2B2DD8033/pinduoduo.app")


def dealData2(data2):
    data3 = []
    list1 = divideList(data2[0], 18)
    data3.append(list1)
    list2 = divideList(data2[1], 20)
    data3.append(list2)
    list3 = divideList(data2[2], 14)
    data3.append(list3)
    list4 = divideList(data2[3], 20)
    data3.append(list4)
    list5 = data2[4]
    data3.append(list5)
    list6 = data2[5]
    data3.append(list6)
    list7 = data2[6]
    data3.append(list7)
    list8 = divideList(data2[7], 14)
    data3.append(list8)
    list9 = divideList(data2[8], 10)
    data3.append(list9)
    return data3

# 等分列表里的数据
def divideList(list, listSize):
    return [list[i:i + listSize] for i in range(0, len(list), listSize)]


def dealDataLast(data):
    # 存储数据列表
    dataList = []

    # 存储前面三个数据 3条
    data1 = []
    for item in data[0]:
        data1.append({
            "序号": item[0],
            "名称": item[1],
            "包名": item[3],
            "版本": item[5],
            "类型": item[7],
            "大小": item[9],
            "更新日期": item[11],
            "安装路径": item[13],
            "权限": item[15],
            "图标": item[17]
        })
    dataList.append(data1)

    # 存储 wifi网络 42条
    data2 = []
    for item in data[1]:
        # print(item)
        data2.append({
            "序号": item[0],
            "MAC": item[1],
            "名称": item[3],
            "最近加入时间": item[5],
            "纬度": item[7],
            "经度": item[9],
            "地平线": item[11],
            "探测时间": item[13],
            "终端IP地址": item[15],
            "加密方式": item[17],
            "连接方式": item[19]
        })
    dataList.append(data2)

    # 存储拍照位置信息 10条
    data3 = []
    for item in data[2]:
        data3.append({
            "序号": item[0],
            "名称": item[1],
            "大小": item[3],
            "类型": item[5],
            "日期": item[7],
            "路径": item[9],
            "经度": item[11],
            "纬度": item[13]
        })
    dataList.append(data3)

    # 应用程序地理位置 7条
    data4 = []
    for item in data[3]:
        data4.append({
            "序号": item[0],
            "应用名称": item[1],
            "用户ID": item[3],
            "用户名": item[5],
            "纬度": item[7],
            "经度": item[9],
            "地点": item[11],
            "详细地址": item[13],
            "时间": item[15],
            "分享对象ID": item[17],
            "来源账号名称": item[19]
        })
    dataList.append(data4)

    # 已删除日历 1条
    data5 = []
    data5.append({
        "序号": data[4][0],
        "概要": data[4][2],
        "地点": data[4][4],
        "备注": data[4][6],
        "是否全天": data[4][8],
        "主题": data[4][10],
        "类型": data[4][12],
        "内容": data[4][14],
        "开始时间": data[4][16],
        "结束时间": data[4][18],
        "提醒时间": data[4][20],
        "优先级": data[4][22],
        "状态": data[4][24]
    })
    dataList.append(data5)

    # 已删除备忘录 1条
    data6 = []
    data6.append({
        "序号": data[5][0],
        "标题": data[5][2],
        "概要": data[5][4],
        "创建时间": data[5][6],
        "修改时间": data[5][8],
        "内容": data[5][10],
        "作者": data[5][12],
        "路径": data[5][14],
    })
    dataList.append(data6)

    # 同步账号 1条
    data7 = []
    data7.append({
        "序号": data[6][0],
        "名称": data[6][1],
        "类型": data[6][2],
        "密码": data[6][3],
    })
    dataList.append(data7)

    # 图片 105条
    data8 = []
    for item in data[7]:
        # print(item)
        data8.append({
            "序号": item[0],
            "缩略图": item[1],
            "文件名称": item[2],
            "大小": item[3],
            "创建时间": item[4],
            "修改时间": item[5],
            "路径": item[7],
            "本地拍摄": item[9],
            "文件MD5": item[11],
            "自拍": item[13],
        })
    # print(data8)
    dataList.append(data8)

    # 缩略图恢复 6条
    data9 = []
    for item in data[8]:
        # print(item)
        data9.append({
            "序号": item[0],
            "文件名称": item[1],
            "大小": item[2],
            "类型": item[3],
            "创建日期": item[4],
            "修改日期": item[5],
            "存储位置": item[7],
            "文件MD5": item[9],
        })
    # print(data9)
    dataList.append(data9)

    return dataList


def savaData(LastData):

    # 1、保存应用信息
    filePath1 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/应用信息.csv"
    with open(filePath1, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号", "名称", "包名", "版本", "类型", "大小", "更新日期", "安装路径", "权限", "图标"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[0]:
            file_csv.writerow(data)

    # 2、保存wifi网络
    filePath2 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/wifi网络.csv"
    with open(filePath2, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","MAC","名称","最近加入时间","纬度","经度","地平线","探测时间","终端IP地址","加密方式","连接方式"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[1]:
            file_csv.writerow(data)

    # 3、保存拍照位置信息
    filePath3 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/拍照位置信息.csv"
    with open(filePath3, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","名称","大小","类型","日期","路径","经度","纬度"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[2]:
            file_csv.writerow(data)

    # 4、保存应用地理位置信息
    filePath4 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/应用地理位置信息.csv"
    with open(filePath4, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","应用名称","用户ID","用户名","纬度","经度","地点","详细地址","时间","分享对象ID","来源账号名称"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[3]:
            file_csv.writerow(data)

    # 5、保存已删除日历信息
    filePath5 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/已删除日历.csv"
    with open(filePath5, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","概要","地点","备注","是否全天","主题","类型","内容","开始时间","结束时间","提醒时间","优先级","状态"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[4]:
             file_csv.writerow(data)

    # 6、保存已删除备忘录信息
    filePath6 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/已删除备忘录.csv"
    with open(filePath6, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","标题","概要","创建时间","修改时间","内容","作者","路径"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[5]:
            file_csv.writerow(data)

    # 7、保存同步账号
    filePath7 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/同步账号.csv"
    with open(filePath7, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","名称","类型","密码"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[6]:
            file_csv.writerow(data)

    # 8、保存图片信息
    filePath8 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/图片信息.csv"
    with open(filePath8, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","缩略图","文件名称","大小","创建时间","修改时间","路径","本地拍摄","文件MD5","自拍"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[7]:
            file_csv.writerow(data)

    # 9、保存缩略图恢复信息
    filePath9 = "D:/研究实习/研究生实习工作任务描述/爬取到的数据/缩略图恢复信息.csv"
    with open(filePath9, "a+", newline="", encoding="utf-8") as file:
        head_file = ["序号","文件名称","大小","类型","创建日期","修改日期","存储位置","文件MD5"]
        file_csv = csv.DictWriter(file, fieldnames=head_file)
        file_csv.writeheader()
        for data in LastData[8]:
            file_csv.writerow(data)

# 测试
if __name__ == '__main__':
    main()
    print("爬取结束")
