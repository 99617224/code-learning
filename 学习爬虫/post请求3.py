import requests

#定义URL
url='https://fanyi.baidu.com/sug'

#定义请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#定义发送的数据
word=input()
data={'kw':word}

#发送请求
res=requests.post(url=url,headers=headers,data=data)

#接收返回数据
code=res.status_code
if code == 200:
    print('请求成功')
    data=res.json()
    if data['errno']==0:
        print('接受成功')
        print(data)
        print(data['data'][0]['k'])
        v=data['data'][0]['v']
        print(v.split(';')[-2])
