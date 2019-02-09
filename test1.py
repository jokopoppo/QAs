from pythainlp.number import *
import deepcut
s = ['ใน', 'ปี', ' ', '2560', ' ', 'ปกเกล้า อนันต์', ' ', 'เล่น', 'ใน', 'ตำแหน่ง', 'กอง', 'กลาง', ' ', 'ให้', 'กับ', 'สโมสรใด']
tmp_q = []
for i in s:
    for w in deepcut.tokenize(i):
        tmp_q.append(w)
s = tmp_q

print(s)