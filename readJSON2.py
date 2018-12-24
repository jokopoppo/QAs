# coding=utf8

import sqlite3
import os
from pprint import pprint
import json
# import deepcut
import time
from heapq import nlargest
from sqlitedict import SqliteDict

def remove_dup(l):
    seen = set()
    newlist = []
    for item in l:
        t = tuple(item)
        if t not in seen:
            newlist.append(item)
            seen.add(t)
    return newlist

def index_shorttest_list(a):
    min_list = ([len(ls) for ls in a])
    return min_list.index(min(min_list))


# initial databased
# conn = sqlite3.connect('TF.db')
# c = conn.cursor()
dict = SqliteDict('db.sqlite', autocommit=True)
begin = time.time()
alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# initial data and test set
index_dir = 'E:/CPE#Y4/databaseTF/dict2/'
file = open("questions_tokenize.json", mode = 'r' , encoding="utf-8-sig")
data = json.load(file)
validate = json.load(open("questions_answer.json", mode = 'r' , encoding="utf-8-sig"))
# validate = [1]
# data = [deepcut.tokenize(s)]
doc = 0
data = data[doc:]
print(data.__len__())
save = 0
string = ''
acc=0
for s in data:
    start = time.time()
    string += "question " + str(doc)
    print("question",doc,s,validate[doc])
    s.sort()
    s = list(set(s))
    search = []
    cantfind = []

    # # find by sqlitedict
    now=None
    for f in range(s.__len__()):
        if(s[f].isspace()):
            continue
        if s[f-1][0] != s[f][0]:
            now = dict.get(s[f][0])

        tmp = None
        if(now != None):
            tmp = now.get(s[f])
        if tmp != None :
            search.append((s[f], tmp))
        else:
            cantfind.append((s[f]))

    # rank by tf-idf
    rank = []
    for i in range(search.__len__()):
        rank.append(search[i][1][0][0])

    # create docs list
    intersection = []
    for i in search:
        intersection.append([])
        for j in range(1,i[1].__len__()):
            try:
                intersection[-1].append([i[1][j][0],i[1][j][4]])
            except IndexError:
                continue
    intersection = [x for _, x in sorted(zip(rank, intersection),reverse=True)]
    intersection=[intersection[index_shorttest_list(intersection)],intersection[0]]
    print(intersection[0].__len__(),intersection[1].__len__())
    answer_index = []
    count = []

    # rank answer answer pool
    for i in intersection:
        for j in i:
            if answer_index.__len__()> 15000:
                break
            if j[0] in answer_index:
                count[answer_index.index(j[0])] += j[1]
            else:
                answer_index.append(j[0])
                count.append(j[1])
    answer_n = nlargest(intersection[0].__len__()+intersection[1].__len__(), count)
    answer = []
    for i in answer_n:
        index = count.index(i)
        answer.append(answer_index[index])
        answer_index.pop(index)
        count.pop(index)
    # print(answer_n)
    print(answer.__len__(),answer[:6])

    # write in text file
    answer = list(answer)
    ans_int = ''
    find = []
    for i in intersection:
        find.append([])
        for j in i:
            find[-1].append(j[0])
    try:
        ans_int = ' ' + str(find[1].index(str(validate[doc]))) + ' '
    except ValueError:
        ans_int = ' cant find in best tf-idf '

    try:
        ans_int += ' ' + str(find[0].index(str(validate[doc]))) + ' '
    except ValueError:
        ans_int += ' cant find in shorttest '

    ########################################################################################

    try:
        if answer.index(str(validate[doc])) < 6 :
            string += ': 1'
        else:
            string += ': 0'
        string += " rank" + str(answer.index(str(validate[doc]))) + ' ||' + ans_int + str(find[1].__len__()) +' '+ str(find[0].__len__()) +' '+ str(cantfind)
    except ValueError:
        string += ": 0 Cant find doc" + ' ||' + ans_int + str(find[1].__len__()) +' '+ str(find[0].__len__()) +' '+ str(cantfind)

    end = time.time()
    print(end - start, 'secs')
    string+= ' '+str(end-start)+ 'secs \n'
    doc+=1
    save+=1
    if save==5 or doc==2000:
        with open("result_tf-idfNew4000.txt", "a" , encoding = "utf-8") as text_file:
            text_file.write(string)
        save = 0
        string = ''
    if doc ==2000:
        break

end = time.time()
print(end - begin, ' secs')
# c.close()
# os.system("shutdown /s /t 90")


