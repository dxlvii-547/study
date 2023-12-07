##  pandas 练习
~~~
调用 import pandas as pd
df=pd.DateFrame({'ID':[1,2,3],
'Name':['A','B','C']})
df.to_excel[C:/Temp/xxx.xlsx]
print ['Done!'] 

## pandas 数据读取 
1.pd.read_csv       csv/tsv/txt
2.pd.read_excel 
3.pd.read_sql

ratings=pd.read_csv(路径)
4.查看前几行
ratings.head()
5.查看数据形状，返回行列
ratings.shape
6.查看列名
ratings.columns
7.查看数据类型 
ratings.dtypes

自己设定的分隔 
fpash = './datas/xx'
shuju = pd.read_csv(
    fpash,
    sep='\t',
    header = None,
    names = ['a','b','c']
)

读取mysql数据库 
import pymysql
conn = pymysql.connet(
    host= '127.00.0',
    user='root',
    password = '123',
    database = 'test',
    charset = 'utf8'
)
mysqlpage = pd.read_mysql (select * from 表明 con=conn)

## 数据结构
DataFrame 二维数据 整个表格 多行多列
Series 类似表格中的一个列 一维数组可以保存任何数据类型
import pandas as pd 
import numpy as np
a = [1,2,3,'a',4]
s1 = pd.series([1,2,3,'a',4])
series  的第一列为索引 第二列为数据 若不指定索引 则索引从0开始
print(s1[2]) 则输出为3

可以指定索引值 
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
根据索引值读数据则为
print(myvar["y"])

可以使用key/value来创建
import pandas as pd
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)

读取json数据
import pandas as pd
df = pd.read_json('sites.json')
print(df.to_string())
可将字典类型数据转化为DF数据
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}                         
df = pd.DataFrame(s)
print(df)

从url中读取json数据
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)

处理嵌套的json数据 
假设嵌套的文件为nested_list.json
df = pd.read_json('nested_list.json')
print(df)
此时再标准化
import pandas as pd
import json
# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)  
~~~
--- 
~~~
Pandas 数据清洗
若要删除包含空字段的行  dropna()
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

1.axis默认为0表示逢空值剔除整行 axis=1表示逢空值剔除整列
2.how默认为any 一行或一列出现一个NA 若设置为how='all'一行或一列都是NA则去除整行
3.thresh 设置需要多少非空值数据才保留
4.subset 设置想要检查的列 若多个列 可以用列名的list作为参数
5.inplace 若设置为True 则计算得到的值直接覆盖之前的值并返回 None修改的是源数据


数据替换  可采用fillna()替换空字段
import pandas as pd
df = pd.read_csv('property-data.csv')
df.fillna(12345, inplace = True)
print(df.to_string())
若替换的是例如PID列的
则改为df['PID'].fillna(12345, inplace = True)

还可以使用均值替换 
import pandas as pd
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mean()
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())
同理 中位数为median() 众数为mode()

-------转换相同格式数据
import pandas as pd
# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

-------将数据进行改变
将age大于120的改为120 
import pandas as pd
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}
df = pd.DataFrame(person)
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120
print(df.to_string())
或删除
df.drop(x, inplace = True)


-------清洗重复数据 
import pandas as pd
persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(persons)
df.drop_duplicates(inplace = True)
print(df)

