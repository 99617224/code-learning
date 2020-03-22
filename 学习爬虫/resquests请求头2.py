import requests
#定义网址
url="https://www.xicidaili.com/"

#定义请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#发起get请求
res=requests.get(url=url,headers=headers)

#获取状态码
code=res.status_code
print(code)

#写入获取的页面
if code == 200:
    with open('./text.html','w') as html:
        html.write(res.text)
