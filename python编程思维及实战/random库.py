import random

random.seed(10)  #种子，不设定的话默认时系统时间

r=random.random()
print(r)
print(random.getstate())
print(random.setstate((10,2,3,5,85,3820876946,3288851063,2607677986,5,85,3820876946)))