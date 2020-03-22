from bs4 import BeautifulSoup
import requests
url= requests.get('http://www.gongzheng.online')
html_doc=url.text

#解析网页
soup=BeautifulSoup(html_doc,'lxml')

#通过标签获取数据
r=soup.title
r3=soup.title.text
r2=soup.p
r4=soup.title.parent.name
# print(r,r2,r3,r4)

#通过find获取数据
r5=soup.find('title')
r6=soup.findAll('a')
r7=soup.find(id='sp-section-2')
r8=r5.text
# print(r5)
# print(r6)
# print(r7)
# print(r8)

#通过CSS选择器获取数据
#通过标签选择元素
print(soup.select('title')[0].text)
#通过id选择元素
print(soup.select('#username-lbl')[0].text)
#通过空格 层级关系获取元素、
print(soup.select('html body span'))
#通过,并列关系获取元素、
print(soup.select('html,body,span'))
