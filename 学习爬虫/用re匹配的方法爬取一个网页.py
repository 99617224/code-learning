import re,requests,json

#定义网址和头信息
url='https://www.lmonkey.com/ask'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
#取得网页
res=requests.get(url,headers)
#爬取想要的数据
res_html=res.text
if res.status_code == 200:
    print('获取网页成功')
    with open('./res.html','w',encoding='utf-8') as fp:
        fp.write(res_html)
    #创建标题、作者、时间的正则匹配
    reg1='<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    title=re.findall(reg1,res_html)
    reg2='<strong>(.*?)</strong>'
    author=re.findall(reg2,res_html)
    reg3='<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    date=re.findall(reg3,res_html)    
#数据存档
data=list(zip(title,author,date))
# print(data)
#常规方式处理数据
# data_list=[]
# for i in data:
#     dic={'title':i[0],'author':i[1],'date':i[2]}
#     data_list.append(dic)
# print(data_list)
#牛逼方法(列表推到式)
data_list=[{'title':i[0],'author':i[1],'date':i[2]} for i in data]
print(data_list)
#数据入库
with open('./data.josn','w',encoding='utf-8') as fp:
    json.dump(data_list,fp)