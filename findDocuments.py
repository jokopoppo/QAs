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

    # segment until no space
    r = []
    for i in s:
        if ' ' in i:
            r.append(i)
            for j in i.split():
                s.append(j)
    for i in r:
        s.remove(i)

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

    # remove least mean tf-idf
    word = []
    pool = []
    search.sort(key=lambda s: s[1][0][0], reverse=True)
    for i in range(4):
        if (search.__len__() > 1):
            search.pop()
        else:
            break
    # word.append(search[0][0])
    # pool.append(search[0][1][1:])

    search.sort(key=lambda s: len(s[1]))
    for i in range(2):
        try:
            word.insert(i, search[i][0])
            pool.insert(i, search[i][1][1:])
        except IndexError:
            break
    # weight shortest in case shortest + best tf-idf
    # for i in range(pool[0].__len__()):
    #     pool[0][i][1] *= 3

    ########################################################################################

    answer_index = []
    count = []

    # rank answer in answer pool
    c = {}
    for i in range(pool.__len__()):
        for k, v in pool[i]:
            try:
                c[k] += v
            except KeyError:
                c[k] = v
    for key, value in c.items():
        answer_index.append(key)
        count.append(value)

    ########################################################################################
    n = 0
    for i in pool:
        n+= i.__len__()
    answer_n = nlargest(n, count)
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
    for i in range(pool.__len__()):
        find.append([])
        for j in pool[i]:
            find[-1].append(j[0])
        try:
            find[i].index(str(validate[doc]))
            ans_int = ' '
        except ValueError:
            ans_int = ' c[' + str(i) + '] '

    ########################################################################################

    try:
        if answer.index(str(validate[doc])) < 6:
            string += ': 1'
        else:
            string += ': 0'
        string += " rank" + str(answer.index(str(validate[doc])))
    except ValueError:
        string += ": 0 cdoc"

    string += ' || [' + str(word) + ']' + ans_int
    for i in range(find.__len__()):
        string += str(find[i].__len__()) + ' '
    string += str(cantfind)

    end = time.time()
    print(end - start, 'secs')
    string += ' ' + str(end - start) + 'secs \n'
    doc += 1
    save += 1
    if save == 100 or doc == 4000:
        with open("result_rLeast1st2nd3rd4th_and_shortest1st2nd.txt", "a", encoding="utf-8") as text_file:
            text_file.write(string)
        save = 0
        string = ''
    if doc == 4000:
        break

# os.system("shutdown /s /t 90")
