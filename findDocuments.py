# coding=utf8

import sqlite3
import os
from pprint import pprint
import json
# import deepcut
import time
from heapq import nlargest
from sqlitedict import SqliteDict

# initial databased
start = time.time()
dict = SqliteDict('doc.sqlite', autocommit=True)
dict = dict['doc']
end = time.time()
print("Time to initial db", end - start)
# initial data and test set
file = open("new_sample_questions_tokenize.json", mode='r', encoding="utf-8-sig")
data = json.load(file)
validate = json.load(open("new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))

doc = 3000
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

    # rank by tf-idf & shortest
    search.sort(key=lambda s: len(s[1]))
    shortest = search[0]
    search.sort(key=lambda s: s[1][0][0], reverse=True)
    best_tfidf = search[0]

    word = [shortest[0], best_tfidf[0]]
    pool = [shortest[1][1:], best_tfidf[1][1:]]
    for i in range(1,search.__len__()):
        word.append(search[i][0])
        pool.append(search[i][1][1:])

    answer_index = []
    count = []

    # rank answer in answer pool
    # for i in pool:
    #     for j in i:
    #         try:
    #             count[answer_index.index(j[0])] += j[1]
    #         except ValueError:
    #             answer_index.append(j[0])
    #             count.append(j[1])

    # rank by single tf-idf
    c={}
    for i in pool :
        for k, v in i:
            try:
                c[k] += v
            except KeyError:
                c[k] = v
    for key, value in c.items():
        answer_index.append(key)
        count.append(value)


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
        ans_int = ' cant find in best tf-idf '

    try:
        find[0].index(str(validate[doc]))
        ans_int += ' '
    except ValueError:
        ans_int += ' cant find in shortest '

    ########################################################################################

    try:
        if answer.index(str(validate[doc])) < 6:
            string += ': 1'
        else:
            string += ': 0'
        string += " rank" + str(answer.index(str(validate[doc]))) + ' || [' + str(word) + ']' + ans_int + str(find[1].__len__()) + ' ' + str(find[0].__len__()) + ' ' + str(cantfind)
    except ValueError:
        string += ": 0 Cant find doc" + ' || [' + str(word) + ']' + ans_int + str(
            find[1].__len__()) + ' ' + str(find[0].__len__()) + ' ' + str(cantfind)

    end = time.time()
    print(end - start, 'secs')
    string += ' ' + str(end - start) + 'secs \n'
    doc += 1
    save += 1
    if save == 100 or doc == 4000:
        with open("result_improve_newDB.txt", "a", encoding="utf-8") as text_file:
            text_file.write(string)
        save = 0
        string = ''
    if doc == 4000:
        break

# c.close()
# os.system("shutdown /s /t 90")

