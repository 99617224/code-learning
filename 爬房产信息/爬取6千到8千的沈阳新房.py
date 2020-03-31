import re
import requests
from bs4 import BeautifulSoup as bs

#设置必要参数
url='https://sy.newhouse.fang.com/house/s/b26000%2C8000/?ctm=1.sy.xf_search.lpsearch_price.4'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
result_dic={

}
#请求信息
res=requests.get(url=url,headers=headers)
res.encoding='"gb2312"'
res_html=res.text
if res.status_code == 200:
#爬取
    soup=bs(res_html,'lxml',)
    print(soup.select(".nlcd_name")[0].text)


#数据编辑

#数据储存