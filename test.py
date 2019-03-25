import os
import json
import usage
from itertools import chain

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

# path = 'E:\CPE#Y4\databaseTF\\new-documents-tokenize\\'
#
# file = os.listdir(path)
#
# word = []
# for i in range(file.__len__()):
#     t = json.load(open(path + file[i], 'r',encoding='utf-8'))
#     print(i)
#     for j in t:
#         word.append(j)
#
# usage.alarm()
# word = set_chain(word)
# print('LEN :',word.__len__())
# with open('all_word.json', 'w', encoding="utf-8") as outfile:
#     json.dump(word, outfile, ensure_ascii=False)

word = json.load(open('all_word_no_space.json', 'r',encoding='utf-8'))
q = json.load(open('test_set\\questions_tokenize.json', 'r',encoding='utf-8'))

print(word.__len__())

all = 0
acc = 0
for i in q:
    for j in i:
        all+=1
        if j in word:
            acc+=1
            # print(j,end=' ')
        else:
            tmp = j.split(' ')
            for k in tmp:
                all+=1
                if k in word:
                    acc += 1
                else:
                    print(k,end=' ')
    print()
print(acc/all)
