import json

def answer_word(doc,answer_begin,answer_end):
    word = ''
    for i in range(answer_begin - 1, answer_end):
        word +=doc[i]
    return word

def extractNumberFromString(string):
    import re
    return re.findall('\d+', string )
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
real_answer = []
question_words = ['กี่', 'ปี', 'เท่า' ,'ใด' , 'ไร' ,'อะไร']
for i in range(a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']

    if answer.isnumeric():
        real_answer.append([i,answer])
        doc = json.load(open('E:\CPE#Y4\databaseTF\documents-tokenize\\'+str(article_id)+'.json','r',encoding='utf-8-sig'))
        sentence_answer = []
        l = 0
        for j in range(doc.__len__()):
            l += doc[j].__len__()
            if l >= answer_begin - 1:
                for k in range(j-15,j+15):
                    try:
                        sentence_answer.append(doc[k])
                    except IndexError:
                        break

                question_index.append([i])
                break

        for k in question[i]:
            for w in question_words:
                if k.endswith(w) or k.startswith(w):
                    for j in sentence_answer:
                        if hasNumbers(j):
                            for num in extractNumberFromString(j):
                                question_index[-1].append(num)
                    break
        question_index[-1][1:] = list(set(question_index[-1][1:]))
        print(question_index[-1])

print("Q:",question_index.__len__(),real_answer.__len__())

test1 = []
test2 = []
for i in real_answer:
    test1.append(i[0])
for i in question_index:
    test2.append(i[0])

print(set(test1) - set(test2))

from sqlitedict import SqliteDict
import time

print("Init db")
start = time.time()
dict = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite', autocommit=True)
dict = dict['doc']
print("Time to initial db", time.time() - start)

check_tfidf = []
for i in question_index :
    if i.__len__() > 2:
        tmp = []
        for j in i[1:]:
            try :
                tmp.append(dict[j[0]][j][0][0])
            except KeyError:
                tmp.append(0)
        check_tfidf.append(i[tmp.index(max(tmp)) + 1])
    else:
        try:
            check_tfidf.append(i[1])
        except IndexError:
            check_tfidf.append(' ')

print(real_answer.__len__())
print(check_tfidf.__len__())

miss = 0
for i in range(real_answer.__len__()):
    if real_answer[i] != check_tfidf[i]:
        miss+=1
print(miss)
# TODO find the way to extract the answer from sentence
