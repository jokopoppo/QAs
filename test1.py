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
from sqlitedict import SqliteDict
import time

start = time.time()
doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc.sqlite', autocommit=True)
dict = doc['doc']
print(time.time() - start)

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
be_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

al = [vowel,e_alphabet,be_alphabet,num]
for a in al :
    for index in a :
        for word in dict[index] :
            tmp = dict[index][word]
            mean = []
            if(tmp[0][1] == -1) :
                print(word)
            for i in range(1,tmp.__len__()) :
                if(tmp[i][1] == -1):
                    tmp[i][1] = 0
                mean.append(tmp[i][1])
            tmp[0][0] = sum(mean)/mean.__len__()
            tmp[0][1] = min(mean)
            dict[index][word] = tmp

start = time.time()
doc['doc'] = dict
doc.commit()
print(time.time() - start)