import requests
from bs4 import BeautifulSoup


rest = requests.get('https://www.baidu.com/')
print(rest)
print(rest.content)

bsobj=BeautifulSoup(rest.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
a_list=bsobj.find_all('a') #获取网页中的所有a标签对象
for a in a_list:
    print(a.get('href'))
