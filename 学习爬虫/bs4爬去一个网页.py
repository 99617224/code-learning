from bs4 import BeautifulSoup
import requests
import json
'''
分析爬去的数据
数据源地址：https://www.lmonkey.com/t
数据内容：文章标题，文章的链接，作者，发布时间
工具：python requests bs4
'''
#定义网址和请求头
url='https://www.lmonkey.com/t'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#发起请求
res=requests.get(url=url,headers=headers)
res_doc=res.text
#判断请求是否成功
print(res.status_code)
if res.status_code==200:
    #解析数据
    soup=BeautifulSoup(res_doc,'lxml')
    
    #获取页面中所有的文章
    divs=soup.find_all('div',class_="list-group-item list-group-item-action p-06")
    # print(divs)
    a=len(divs)-1
    result_list=[]
    for i in divs[0:a]:
        t=i.find('div',class_="topic_title mb-0 lh-180")
        a_dict={'title':t.text.split("\n")[0],'url':i.a['href'],'author':i.strong.a.text,'date':i.span['title']}
        result_list.append(a_dict)
    #

print(result_list)
#写入数据
with open('./data.josn','w') as fp:
    json.dump(result_list,fp)
    