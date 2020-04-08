'''#获取用户输入的参数
keywod=input('请输入要搜索的关键字：')
#调用函数进行数据爬取，可以指定关键字和下载页数
data_List=getpages(keywod,2)
#调用函数，保存数据
saveImg(data_List,'路径')'''
import requests
import os
def getpages(keyword,num):
    url='https://image.baidu.com/search/acjson'
    urls=[]
    #循环页码数
    params=[]
    for i in range(30,30*num+30,30):
        params.append({'tn':'resultjson_com',
            'ipn':'rj',
            'ct':'201326592',
            'is':'',
            'fp':'result',
            'queryWord':keyword,
            'cl':'2',
            'lm':'-1',
            'ie':'utf-8',
            'oe':'utf-8',
            'adpicid':'',
            'st':'-1',
            'z':'',
            'ic':'',
            'hd':'',
            'latest':'',
            'copyright':'',
            'word':keyword,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face':'0',
            'istype':'2',
            'qc':'',
            'nc':'1',
            'fr':'',
            'expermode':'',
            'force':'',
            'pn':i,
            'rn':'30',
            'gsm':'1e',
            '1586004293686':'',})
    
    for i in params:
         #向每个URL发起请求
        res=requests.get(url=url,params=i)
        urls.append(res.json()['data'])
    return urls




def saveImg(data,dir):
    #检测文件夹是否存在
    if not os.path.exists(dir):
        os.mkdir(dir)
    for i in data:
        count=1
        for x in i:
            if x.get('thumbURL') !=None:
                print(f"下载图片{x.get('thumbURL')}")
                #向图片地址发起请求
                imgs=requests.get(x.get('thumbURL'))
                open(f"{dir}/{count}.jpg",'wb').write(imgs.content)
                count+=1

data=getpages('大彪',5)
saveImg(data,'./大彪')





