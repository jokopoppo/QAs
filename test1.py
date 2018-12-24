# import numpy as np
# a=[[['a',2],['b',5]] ,[['c',2],['a',8]]]
#
# c={}
#
#
#
# for key, value in c.items():
#     print(key,value)
import json

file = open('result_improve_newDB.txt','r',encoding='utf-8-sig')

acc=0
data = []
for i in file:
    i=i.split()
    print(i)
    data.append(i)
    acc+=int(i[2])

print(acc/data.__len__())