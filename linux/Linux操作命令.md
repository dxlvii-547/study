# Linux常用命令


## cd命令
~~~ 
进入目录 
cd wenjianming
切换名录
cd /root/Documents 切换到目录
cd ./path  切换到当前目录下的path目录中
cd ../path 切换到上层目录的path目录中 
.表示当前目录 ..表示上一层目录
返回上一层目录 
cd .. 
返回上层目录的上层目录 
cd ../..
返回刚才进入的目录 
cd - 
~~~
## ls命令
~~~
用来查看文件与目录的命令 
-l 以长数据串形式列出当前目录下数据文件和目录 
ll 为ls -l简写 
-a 列出全部的文件 连同隐藏文件一切列出
-d 仅列出目录本身 
-h 将文件容量以易读方式列出(GB,KB)
-R 连同子目录的内容一起列出(递归列出)
举例
ls -I列出当前目录下的数据文件和目录 
ls -IR长数据串形式列出当前目录下所有文件
~~~
## pwd命令
~~~
pwd 表示当前目录的绝对路径
--- 如何查看文本文件
假设当前路径有个readme文件 想查看
cat readme.md   但看不全文件过大的时候 可以用以下来看开头
head readme.md 
若想看前两行
head --lines=2 readme.md
若想看尾
tail --lines=2 readme.md
看全文 
less readme.md 

--- 如何编辑文本文件 
nano readme.md 
nano的优势是底部有快捷操作指令
或是 
vim readme.md vim进去后是浏览模式 此时按insert进入修改模式  退出按esc键退出编辑模式 再按:q 再退出 :w 是修改  :!q是强制退出
~~~

--- 
如何查看文件的属性 如何确认文件的位置<br />
where readme.md
<br />
file readme.md <br />
## 打印 
~~~
打印
echo 
打印变量 
h="hello"
echo $h 
可以自由连接 
echo "avdjisa$h"
~~~
## 修改文件名
~~~
假设有很多文件week01  week02 ... week99 
mv  原名字 修改后的名字
批量修改
for ff in week?? (week??为week开头两个字符结尾的文件)
for> do 
for> echo $ff
for> done 
打印FF
若要修改去掉全部week 仅显示为01-99
for> do 
for>  ${ff#week}
for> done 
若要变更chapter01
for> do 
for> chapter${ff#week}
for> done 
其中 
${ff#week}为掐头操作
${ff%week}为去尾操作
~~~
## 安装软件

~~~
yum程序  自动化安装工具
yum 
-y 自动确认 无需手动确认安装或卸载过程
install 
remove 
search 
yum -y install wget 
注：需要root权限 可以用su切换到root 
su - root 
ctrl + d 可以快速回到上一个账号
--- 创建文件夹 
mkdir wenjian
~~~

## 上传下载 
~~~
finalshell工具

~~~

 