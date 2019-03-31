import os
import json
import usage
from itertools import chain
import re

def set_chain(x):
    return list(set(chain(*x)))

def space_segment(l):
    len_l = l.__len__()
    for i in range(len_l-1,-1,-1):
        if ' ' in l[i]:
            tmp = l[i].split(' ')
            l.pop(i)
            for j in tmp:
                l.append(j)
        print(i,'/',len_l)

    return list(set(l))

path = 'E:\CPE#Y4\databaseTF\\new-documents-tokenize\\'

file = os.listdir(path)
acc = 0
for i in range(0,file.__len__()):
    t = json.load(open(path + file[i], 'r',encoding='utf-8'))
    # print(t)
    for j in range(t.__len__()):
        r = []
        new_tj = []
        for k in range(t[j].__len__()):
            if not t[j][k].isspace() and ' ' in t[j][k]:
                acc +=1
                print(file[i],t[j][k] , end=' ')
    #             tmp = re.split(r'(\s+)', t[j][k])
    #             for l in tmp:
    #                 new_tj.append(l)
    #         else:
    #             new_tj.append(t[j][k])
    #     t[j] = new_tj
    # with open(path + file[i], 'w', encoding='utf-8') as outfile:
    #     json.dump(t, outfile, ensure_ascii=False)
    print(i, '/', file.__len__())
print(acc)
# os.system("shutdown /s /t 30")
