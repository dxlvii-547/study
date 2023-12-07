# 爬虫
from bs4 import BeautifulSoup  #网页解析获取数据
import re # 正则表达式
import urllib.request,urllib.error #制定url 
import xlwt # 写入excel
import sqlite3 # 数据库操作 


def main():
    baseurl = 'https://movie.douban.com/top250?start='
  #1.爬取网页
def getDate(baseurl):
    datalist = []
    return datalist #返回数据
    #2.解析数据

    #3.保存数据
    savepath = './movie.xls'
def savaDate(savapath)
    





if __name__ == '__main__':  #当程序执行时
    #调用函数
    main()



# 基础概念

# 一、获取一个get请求
# import urllib.request 
# response = urllib.request.urlopen('http://www.baidu.com/')
# html = response.read().decode('utf-8') # 读取网页内容 并利用utf-8解码
# print(html)
# 二、获取一个post请求 
# import urllib.request 
# import urllib.parse
# 先给一个表单
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding = 'utf-8')  #方法，转化为二进制数据包
# response = urllib.request.urlopen('http://httpbin.otg/',data = data )
# html = response.read().decode('utf-8')
# print(html)
# post请求需要将数据进行规定的封装
# 三、请求超时
# 加上一个连接超时限制 可以加在url后
# response = urllib.request.urlopen('http://www.baidu.com/get',timeout = 0.01)






pip install pyftpdlib