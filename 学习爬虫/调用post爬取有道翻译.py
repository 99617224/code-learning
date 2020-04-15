import requests
#定义前期参数
data={
    'i':'大彪子',
    'doctype':'json'
    }

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

#发起请求

res=requests.post(url=url,data=data,headers=headers)

print(res.status_code)
# print(res.content.decode('utf-8'))
# print(res.json()) #如果返回的时json数据可以直接解析
res_data=res.json()
if res_data['errorCode'] == 0:
    print(res_data['translateResult'][0][0]['tgt'])