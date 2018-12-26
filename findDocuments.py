# coding=utf8

import sqlite3
import os
from pprint import pprint
import json
# import deepcut
import time
from heapq import nlargest
from sqlitedict import SqliteDict
import numpy as np

# initial databased
start = time.time()
dict = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc.sqlite', autocommit=True)
dict = dict['doc']
end = time.time()
print("Time to initial db", end - start)
# initial data and test set
file = open("test_set\\new_sample_questions_tokenize.json", mode='r', encoding="utf-8-sig")
data = json.load(file)
validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))

doc = 0
data = data[doc:]
print(data.__len__())
save = 0
string = ''

for s in data:
    start = time.time()
    string += "question " + str(doc)
    print("question", doc, s, validate[doc])
    s.sort()
    s = list(set(s))
    search = []
    cantfind = []

    # # find by sqlitedict

    for f in range(s.__len__()):
        if (s[f].isspace()):
            continue
        if (s[f][0] == ' ') or (s[f][-1] == ' '):
            s[f] = s[f].strip()

        try:
            tmp = dict[s[f][0]][s[f]]
            search.append((s[f], tmp))
        except KeyError:
            cantfind.append((s[f]))

    ########################################################################################

    # rank by tf-idf & shortest
    word = []
    pool = []
    search.sort(key=lambda s: s[1][0][0], reverse=True)
    if(search.__len__() > 2):
        search.pop()
    word.append(search[0][0])
    pool.append(search[0][1][1:])

    search.sort(key=lambda s: len(s[1]))
    word.insert(0,search[0][0])
    pool.insert(0,search[0][1][1:])


    ########################################################################################

    answer_index = []
    count = []

    # rank answer in answer pool
    c={}
    for i in range(pool.__len__()) :
        for k, v in pool[i]:
            if(i==0): # # weight shortest in case shortest + best tf-idf
                v*=3
            try:
                c[k] += v
            except KeyError:
                c[k] = v
    for key, value in c.items():
        answer_index.append(key)
        count.append(value)

    ########################################################################################

    answer_n = nlargest(pool[0].__len__() + pool[1].__len__(), count)
    answer = []
    for i in answer_n:
        index = count.index(i)
        answer.append(answer_index[index])
        answer_index.pop(index)
        count.pop(index)
    # print(answer_n)
    print(answer.__len__(), answer[:6])

    # write in text file
    answer = list(answer)
    ans_int = ''
    find = []
    for i in pool:
        find.append([])
        for j in i:
            find[-1].append(j[0])
    try:
        find[1].index(str(validate[doc]))
        ans_int = ' '
    except ValueError:
        ans_int = ' cb '

    try:
        find[0].index(str(validate[doc]))
        ans_int += ' '
    except ValueError:
        ans_int += ' cs '

    ########################################################################################

    try:
        if answer.index(str(validate[doc])) < 6:
            string += ': 1'
        else:
            string += ': 0'
        string += " rank" + str(answer.index(str(validate[doc]))) + ' || [' + str(word) + ']' + ans_int + str(find[1].__len__()) + ' ' + str(find[0].__len__()) + ' ' + str(cantfind)
    except ValueError:
        string += ": 0 cdoc" + ' || [' + str(word) + ']' + ans_int + str(
            find[1].__len__()) + ' ' + str(find[0].__len__()) + ' ' + str(cantfind)

    end = time.time()
    print(end - start, 'secs')
    string += ' ' + str(end - start) + 'secs \n'
    doc += 1
    save += 1
    if save == 100 or doc == 4000:
        with open("result_remove_leastTF-IDF_weight_shortest_and_bestTF-IDF.txt", "a", encoding="utf-8") as text_file:
            text_file.write(string)
        save = 0
        string = ''
    if doc == 4000:
        break

# os.system("shutdown /s /t 90")

