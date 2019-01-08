# coding=utf8

import json
from pythainlp.corpus import stopwords
import time
import pythainlp.tokenize
start = time.time()

words = stopwords.words('thai')
q = json.load(open("test_set\\new_sample_questions_tokenize.json", mode='r', encoding="utf-8-sig"))
validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
n_q = json.load(open("no_stop_words_questions_.json", mode='r', encoding="utf-8-sig"))

questions = []
for question in range(q.__len__()) :
    print(q[question],end= " ")
    new = []
    for i in range(q[question].__len__()):

        cut = pythainlp.word_tokenize(q[question][i],engine='deepcut')
        for j in cut :
            if j not in words:
                new.append(j)

    questions.append(new)
    print(questions[-1])

json.dump(questions, open("no_stop_words_questions_.json", "w"), ensure_ascii=True)

print(time.time() - start)