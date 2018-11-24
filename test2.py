import json
from pprint import pprint
n1 = 'result_tf-idf.txt'
n2 = 'result_newAlgorithm.txt'
file = open(n2,'r',encoding='utf-8')

data = []

for i in file:
    data.append(i.split())

for i in data:
    print(i)

acc=0
for i in data:
    if i[3][0]== 'r' :
        acc+=1

print(acc)