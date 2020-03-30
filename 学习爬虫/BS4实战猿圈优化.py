from bs4 import BeautifulSoup
import requests
import json
'''
分析爬去的数据
数据源地址：https://www.lmonkey.com/t
数据内容：文章标题，文章的链接，作者，发布时间
工具：python requests bs4
'''
#封装类
class bs4yq():
    #定义属性
    url='https://www.lmonkey.com/t'
    headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
    #响应的源代码存放的位置
    res_html=None
    #存放数据的LIST
    result_list=[]
    
    #初始化方法
    def __init__(self):
        #发起请求
        res=requests.get(self.url,headers=self.headers)
        if res.status_code == 200:
            self.res_html=res.text
            if self.ParseData:
                self.WriteJosn()
                print('请求成功，数据写入文件')
                print(self.result_list)
        else:
            print('请求失败')
    #解析html数据
    def ParseData(self):
        try:
            soup=BeautifulSoup(self.res_html,'lxml')
        
            #获取页面中所有的文章
            divs=soup.find_all('div',class_="list-group-item list-group-item-action p-06")
            # print(divs)
            a=len(divs)-1
            for i in divs[0:a]:
                t=i.find('div',class_="topic_title mb-0 lh-180")
                a_dict={'title':t.text.split("\n")[0],'url':i.a['href'],'author':i.strong.a.text,'date':i.span['title']}
                self.result_list.append(a_dict)
            return self.result_list
        except:
            return False
    #写入json数据
    def WriteJosn(self):
            try:
                if self.result_list !=[]:
                    with open ('./data.josn','w') as fp:
                        josn.dump(self.result_list,fp)
                        return True
            except:
                print('无法获取解析的数据')
                return False

bs4yq()