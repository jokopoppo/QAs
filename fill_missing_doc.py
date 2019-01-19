import json
from sqlitedict import SqliteDict
import time
from usage import alarm

def check_tokenizeJSON(num):
    n_q = json.load(open("no_stop_words_questions_.json", mode='r', encoding="utf-8-sig"))
    q = json.load(open("test_set/new_sample_questions_tokenize.json", mode='r', encoding="utf-8-sig"))
    answer = json.load(open("test_set/new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
    print(q[num] , answer[num])
    db = json.load(
        open("E:\CPE#Y4\databaseTF\documents-tokenize\\" + str(answer[num]) + ".json", mode='r', encoding="utf-8-sig"))

    print(db)

def check_cdoc(path):
    file = open(path, mode='r', encoding="utf-8-sig")
    q = []
    word = []
    for i in file:
        if 'c[0]' in i:
            tmp = int(i.split('rank')[1].split()[0])
            if tmp > 25 :
                q.append(int(i.split()[1].replace(':','')))
                l = i.split('[[')[1].split(']]')[0].split(',')
                for j in range(l.__len__()):
                    l[j] = l[j].strip()
                    l[j] = l[j].replace("'", "")
                word.append(l)

    print(q.__len__())
    return q,word

def fill_missing():
    doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite',autocommit=True)
    dict = doc['doc']

    dir = "result\\result_q_weight5_fill_missing.txt"
    q, word = check_cdoc(dir)
    answer = json.load(open("test_set/new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
    print(word.__len__())

    for i in q:
        print(i)
        for w in word[i][:2]:
            if w.isspace() or (not w):
                continue
            print("WORD :",w , [str(answer[i]), dict[w[0]][w][0][0]])
            dict[w[0]][w].append([str(answer[i]), dict[w[0]][w][0][0]])
            print("INDEX :", dict[w[0]][w][-1])
    start = time.time()
    doc['doc'] = dict
    doc.commit()
    print(time.time() - start)
    return dict

# check_tokenizeJSON(25)

# q,ww = check_cdoc('result/result_q_weight5_fill_cant_find.txt')
# # print(ww)
#
# word = []
# for i in ww :
#     word.append(i[0])
# print(word.__len__(),word)
#
# answer = json.load(open("test_set/new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
# doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite',autocommit=True)
# dict = doc['doc']
#
# for i in range(q.__len__()):
#     if word[i].isspace() or (not word[i]):
#         continue
#     print("WORD :",word[i] , [str(answer[q[i]]), dict[word[i][0]][word[i]][0][0]])
#     dict[word[i][0]][word[i]].append([str(answer[q[i]]), dict[word[i][0]][word[i]][0][0]])
#     print("INDEX :",dict[word[i][0]][word[i]][-3] ,dict[word[i][0]][word[i]][-2],dict[word[i][0]][word[i]][-1])
#
# start = time.time()
# doc['doc'] = dict
# doc.commit()
# print(time.time() - start)
# alarm()
#
