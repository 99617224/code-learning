import requests

url='http://www.gongzheng.online'

res=requests.get(url=url)
# print(res.status_code) 
# print(res.content.decode('utf-8'))
# print(res.headers)
print(res.text)
