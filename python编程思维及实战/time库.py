import time
# print(time.gmtime()) #取得当前的时间
# print(time.time())   #取得一个从计时起点（1970年1月1日）开始到现在的浮点数（当时间戳用）
# print(time.localtime()) #返回本地时间
# print(time.mktime(time.gmtime())) #把时间对象转换成浮点数
# print(time.asctime())  #字符串形式表达时间

# time.sleep(5) #休眠计时
print(time.get_clock_info('monotonic'))