from bs4 import BeautifulSoup # 网页解析，获取数据
import re   # 正则表达式
import urllib.request,urllib.error  # 指定URL，获取指定网页数据
import xlwt # 进行excel操作
# import _sqlite3 # 数据库
import csv

# 定义为全局变量
# r表示忽视所有特殊符号
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')     # 创建正则表达式，表示规则（字符串模式）
# 影片图片的链接规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  # re.S 让换行符包含在字符中
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价的人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    dataList = getData(baseUrl)
    # 2、解析数据
    # 3、保存数据
    # savePath = "豆瓣电影Top250.xls"   # 保存为excel格式的数据
    # saveData(dataList,savePath)

    savePath2 = "豆瓣电影Top250.csv"    # 保存为csv文件格式的数据
    saveData2(dataList,savePath2)
    # askURL(baseUrl)

# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10):
        # 调用获取页面的信息函数10次
        url = baseUrl + str(i*25)
        # 保存获取到的网页源码
        html = askURL(url)

        # 2、逐一解析网页，在for循环里面，一个网页解析一遍
        soup = BeautifulSoup(html,"html.parser")
        # 查找符合要求的字符串。查找div标签中class="item"的内容。class_要加下划线，与关键字区分
        for item in soup.find_all('div',class_="item"):
            # print(item) # 测试：查看电影item的全部信息
            data = [] # 保存一部电影的所有信息
            item = str(item) # 转换成字符串，方便比较
            # print(item)
            # break;
            # 获取到影片详情的链接
            link = re.findall(findLink,item)[0]     #re库通过正则表达式查找指定的字符串
            data.append(link)
            # 添加链接
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)                     # 添加图片

            titles = re.findall(findTitle,item)     # 片名可能有中文名，英文名
            if (len(titles)==2):
                ChineseName = titles[0]
                data.append(ChineseName)                    # 添加中文名
                EnglishName = titles[1].replace("/","")     # 把前面的\去掉
                data.append(EnglishName)                    # 添加英文名
            else:
                data.append(titles[0])
                data.append(' ')    # 外国名留空，统一格式

            rating = re.findall(findRating,item)[0]
            data.append(rating)     # 添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)   # 添加评价的人数

            inq = re.findall(findInq,item)
            if(len(inq)!=0):
                inq = inq[0].replace("。","")    # 去掉句号
                data.append(inq)                 # 添加概述
            else:
                data.append("")                  # 留空，统一格式

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)  # 用第二个参数替换第一个参数的意思。即去掉<br/>
            bd = re.sub('/',"",bd)                  # 替换/
            data.append(bd.strip())                 # 添加影片相关内容，去掉钱前后的空格

            dataList.append(data)   # 把处理好的一部电影信息放入dataList

    print(dataList)
    return dataList

# 保存数据,保存为excel表格的数据
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象，相当于一个文件
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价人数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) # 列名
    for i in range(0,250):
        print(f'第{i+1}条')
        data = dataList[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据

    book.save(savePath)  # 保存数据表

# 保存数据,保存为csv表格的数据
def saveData2(dataList,savePath):
    fp = open(savePath,'a+',newline="",encoding="utf-8")
    csv_fp = csv.writer(fp) # 处理成支持CSV文件操作的对象（句柄）
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价人数","概况","相关信息")
    csv_fp.writerow(col) # 列名
    for i in range(0,250):
        print(f'第{i+1}条')
        data = dataList[i]
        csv_fp.writerow(data)  # 表示写入一行数据
    fp.close()


# 得到一个指定的URL网页内容
def askURL(url):
    # 模拟浏览器向服务器发请求
    head = {
        # 告诉服务器我们是怎样的浏览器，能接受怎样的服务数据
        # 注意空格，不然会报418错误，被服务器识别出来我们是爬虫而不是浏览器
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.ri / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    # 接受数据
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        # 打印错误的代码
        if hasattr(e,"code"):
            print(e.code)
        # 打印错误的原因
        if hasattr(e,"reason"):
            print(e.reason)

    return html



if __name__ == '__main__':
    # 调用函数
    main()
    print("爬取完毕")

