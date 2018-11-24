from sqlitedict import SqliteDict,SqliteMultithread
import sqlitedict
import sqlite3
import sys
import time
import json
from pprint import pprint

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
be_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dict = SqliteDict('db.sqlite',flag='r', autocommit=True)

a=['สุนัข', 'ตัว', 'แรก', 'รับ', 'บท', 'เป็น', 'เบน', 'จี้', 'ใน', 'ภาพยนตร์', 'เรื่อง', ' ', 'Benji', ' ', 'ที่', 'ออก', 'ฉาย', 'ใน', 'ปี', ' ', 'พ.ศ.', ' ', '2517', ' ', 'มี', 'ชื่อ', 'ว่า', 'อะไร']
a.sort()
print(a)
find = []
t = 0
# for word in a :
#     begin = time.time()
#
#     tmp = None
#     try:
#         find.append(dict[word[0]][word])
#     except KeyError:
#         continue
#
#     end = time.time()
#
#     t += (end - begin)
#     print(end-begin)
index_dir = 'E:/CPE#Y4/databaseTF/dict2/'
file = open(index_dir + 'เ.json','r',encoding='utf-8-sig')
data = json.load(file)

for k in data:
    print(data[k][0])
print(t)