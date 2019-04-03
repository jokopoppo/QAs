# coding=utf8

import os
import json
import time
from heapq import nlargest
from sqlitedict import SqliteDict
from pythainlp.corpus import wordnet, stopwords
from usage import alarm, rreplace


def write_result():
    # write in text file

    return


def findDocuments():
    # initial databased
    start = time.time()
    dict = SqliteDict('E:\\CPE#Y4\\databaseTF\\lastest_db\\new-db.sqlite', autocommit=True)
    dict = dict['doc']
    end = time.time()
    print("Time to initial db", end - start)

    # initial data and test set
    q = open('test_set\\new_sample_questions_tokenize.json', mode='r', encoding="utf-8-sig")
    data = json.load(q)
    # validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))

    doc = 0
    data = data[doc:]
    print(data.__len__())
    string = ''
    question_words = stopwords.words('thai')
    question_words.append('กี่')
    question_words.append('ใด')

    test_output = []
    no_word = []
    for s in data:
        string += "question " + str(doc)
        print("question", doc, s)

        # segment until no space and do rule-based
        suffix = ['คือ', 'กี่', 'ใด']
        r = []
        for i in s:
            if ' ' in i:
                for j in i.split():
                    s.append(j)
                r.append(i)
                continue
            for j in suffix:
                if i.endswith(j) or i.startswith(j):
                    s.append(rreplace(i, j, ' ', 1))
                    r.append(i)
                    break
        for i in r:
            s.remove(i)
        ########################################################################################

        s.sort()
        s = list(set(s))
        search = []
        cantfind = []

        # # find by sqlitedict

        for f in range(s.__len__()):
            if (s[f].isspace()) or (s[f] in question_words):
                continue
            if (s[f][0] == ' ') or (s[f][-1] == ' '):
                s[f] = s[f].strip()

            try:
                tmp = dict[s[f][0]][s[f]]
                search.append((s[f], tmp))

            except KeyError:  # # if no index find by synonyms
                cantfind.append(s[f])
                synonyms = []
                for syn in wordnet.synsets(s[f]):
                    for i in syn.lemma_names('tha'):
                        synonyms.append(i)

                if s[f] in synonyms:
                    synonyms.remove(s[f])
                for i in synonyms:
                    try:
                        tmp = dict[i[0]][i]
                        search.append((i, tmp))
                        break
                    except KeyError:
                        cantfind.append(i)
        no_word.append(cantfind)
        ########################################################################################

        # remove least mean tf-idf
        word = []
        pool = []
        search.sort(key=lambda s: s[1][0][0], reverse=True)
        for i in range(0):
            if (search.__len__() > 2):
                search.pop()
            else:
                break

        search.sort(key=lambda s: len(s[1]))
        for i in range(search.__len__()):
            try:
                word.append(search[i][0])
                pool.append(search[i][1][1:])
            except IndexError:
                break

        ########################################################################################

        answer_index = []
        count = []

        # rank answer in answer pool
        c = {}
        weight = [5, 1]
        for i in range(pool.__len__()):
            for k, v in pool[i]:
                try:
                    if i < weight.__len__():
                        c[k] += v * weight[i]
                    else:
                        c[k] += v
                except KeyError:
                    if i < weight.__len__():
                        c[k] = v * weight[i]

        for key, value in c.items():
            answer_index.append(key)
            count.append(value)

        ########################################################################################
        answer_n = nlargest(count.__len__(), count)
        answer = []
        for i in answer_n:
            index = count.index(i)
            answer.append(answer_index[index])
            answer_index.pop(index)
            count.pop(index)

        print(answer.__len__(), answer[:6])
        test_output.append(answer)  ### return this .
        doc += 1

    return test_output, no_word


# os.system("shutdown /s /t 30")

test_output, no_word = findDocuments()
alarm()

with open('test_output.json', 'w', encoding="utf-8") as outfile:
    json.dump(test_output, outfile, ensure_ascii=False)
with open('no_word.json', 'w', encoding="utf-8") as outfile:
    json.dump(no_word, outfile, ensure_ascii=False)
