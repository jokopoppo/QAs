import json
import tensorflow as tf
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)
from gensim.models import Word2Vec
import numpy as np
from pythainlp.number import *


def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b) / (1.0 * max(len(a), len(b)))


def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()


def extractNumberFromString(string):
    import re
    return re.findall('\d+', string)


def hasNumbers(inputString):
    for i in thai_number_text:
        if inputString.startswith(i) or inputString.endswith(i):
            return True
    return any(char.isdigit() for char in inputString)


def make_sentence_answer(article_id, answer_begin, n=15):
    doc = json.load(
        open('E:\CPE#Y4\databaseTF\documents-tokenize\\' + str(article_id) + '.json', 'r',
             encoding='utf-8-sig'))
    sentence_answer = []
    l = 0
    for j in range(doc.__len__()):
        l += doc[j].__len__()
        if l >= answer_begin - 1:
            for k in range(j - n, j + n):
                try:
                    sentence_answer.append(doc[k])
                except IndexError:
                    break
            break
    return sentence_answer


def check_question_type(a, question):
    c = a.split()
    n = a.count(' ')

    if n == 0:
        return c[0] in question
    else:
        return c[1] in question and question[question.index(c[1]) - n] == c[0]


def find_question_word(question, question_words):
    for w in question_words:
        c = w.split()
        n = w.count(' ')
        if check_question_type(w, question):
            if n == 0:
                return [question.index(c[0]), c[0]]
            else:
                return [question.index(c[1]), c[1]]


def find_candidate(possible_answer, doc_id, sentence_answer, l):
    words = []
    words_index = []
    for k in range(sentence_answer.__len__()):
        if sentence_answer[k] != ' ' and not sentence_answer[k].isnumeric():
            try:
                words.append(wv_model.wv[sentence_answer[k]])
                words_index.append(k)
            except KeyError:
                continue
    words = np.asarray(words)
    predictions = classify_model.predict(words)
    predicted_lalel = []
    label = l
    for n in range(2):
        for k in range(predictions.__len__()):
            tmp = np.argmax(predictions[k]) + 2
            predicted_lalel.append(tmp)
            if tmp == label:
                possible_answer.append(sentence_answer[words_index[k]])
                doc_id.append(words_index[k])
        if possible_answer.__len__() > 0:
            break
        else:
            label = max(set(predicted_lalel), key=predicted_lalel.count)

    return possible_answer, doc_id


def relevance_score(question, sentence, candidate, question_word):
    a = []
    question_word_index = question.index(question_word)
    l = 2 * question.__len__()
    for i in candidate:
        a.append([])
        for j in range(i - l, i + l):
            if (i != j) and (0 <= j < sentence.__len__()) and (sentence[j] in question):
                if question.index(sentence[j]) < question_word_index:
                    a[-1].append([question.index(sentence[j]), j, 0.5])
                else:
                    a[-1].append([question.index(sentence[j]), j, 0.25])
        # print(a[-1])

    m = question.__len__() - 1

    score = []
    for i in range(a.__len__()):
        tmp = 0
        for j in a[i]:
            tmp += (1 - abs(j[1] - candidate[i]) / l) * (1 - abs(j[0] - question_word_index) / m)
        score.append(tmp)

    return score


def find_answer_word():
    print(i, s)
    print(possible_answer[-1])
    print(question_word_index, question[i])
    print(sentence_answer, doc_id[-1])

    score = relevance_score(question[i], sentence_answer, doc_id[-1][1:], question_word_index[1])
    all_rs.append(score)
    doc_id[-1].insert(1, sentence_answer[doc_id[-1][score.index(max(score)) + 1]])


a = json.load(open('test_set/new_sample_questions.json', encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี', 'ใคร', 'ว่า', 'อะไร']
question_type = [
    ['กี่', 'ปี ใด', 'ปี อะไร', 'พ.ศ.  อะไร', 'ค.ศ.  อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'พ.ศ. ใด', 'พ.ศ.  ใด', 'ค.ศ. ใด',
     'ค.ศ.  ใด', 'เท่า ไร', 'เท่า ไหร่', 'เท่า ใด', 'คริสต์ศักราช ใด', 'จำนวน ใด']
    , ['เมื่อ ไร', 'เวลา ใด', 'วัน ใด', 'เมื่อ ใด', 'วัน ที่']  # date format
    , ['ใคร', 'ว่า อะไร', 'ชื่อ อะไร', 'คน ใด', 'คน ไหน', 'คือใคร', 'ผู้ ใด']  # human name
    , ['ประเทศ ใด', 'ประเทศ อะไร']
    , ['จังหวัดใด', 'จังหวัด ใด', 'จังหวัด อะไร']
    , ['เมืองใด', 'เมือง ใด', 'เมือง อะไร']
    , ['ภาค ใด']
    , ['แคว้น ใด']
    , ['ทวีปใด', 'ทวีป อะไร', 'ทวีป ใด', 'ภูมิภาค ไหน']
    , ['ที่ ไหน', 'ที่ ใด']  # where
    , ['อะไร', 'อย่าง ไร', 'ใด', 'ไหน']  # other what, other dai, other nhai
]
thai_number_text = [u'หนึ่ง', u'สอง', u'สาม', u'สี่', u'ห้า', u'หก', u'เจ็ด', u'แปด', u'เก้า', u'สิบ', u'สิบเอ็ด']

wrong = 0
all_rs = []
possible_answer = []
n = 0

wv_model = Word2Vec.load("E:\CPE#Y4\databaseTF\word2vec_model_lastest\word2vec.model")

classify_model = tf.keras.models.load_model(
    'model.h5py',
    custom_objects=None,
    compile=True
)

for i in range(wrong, a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']
    sentence_answer = make_sentence_answer(article_id, answer_begin)

    real_answer.append(answer)
    possible_answer.append([])
    doc_id.append([article_id])
    s = ''.join(question[i])
    for l in range(question_type.__len__()):
        if any(check_question_type(k, question[i]) for k in question_type[l]):
            if l > 1:
                possible_answer[-1], doc_id[-1] = find_candidate(possible_answer[-1], doc_id[-1], sentence_answer, l)
                question_word_index = find_question_word(question[i], question_type[l])
                find_answer_word()
            else:
                for k in range(sentence_answer.__len__()):
                    if hasNumbers(sentence_answer[k]):
                        doc_id[-1].append(k)
                        possible_answer[-1].append(sentence_answer[k])
                question_word_index = find_question_word(question[i], question_type[l])
                find_answer_word()
            break

        elif l == 10 and not any(check_question_type(k, question[i]) for k in question_type[l]):
            print("\n#############################\n")
            tmp_q = []
            for q in question[i]:
                tmp = []
                for w in question_type[l]:
                    tmp.append(similar(q, w))
                tmp_q.append([question[i].index(q), max(tmp)])
            tmp_q.sort(key=lambda s: s[1], reverse=True)
            question_word_index = [tmp_q[0][0], question[i][tmp_q[0][0]]]
            possible_answer[-1], doc_id[-1] = find_candidate(possible_answer[-1], doc_id[-1], sentence_answer, l)

            find_answer_word()

print(n)

string = ''
miss = 0
for i in range(real_answer.__len__()):

    if real_answer[i] != doc_id[i][1]:
        tmp = similar(real_answer[i], doc_id[i][1])
        string += str(i) + ' ' + str(real_answer[i]) + ' ' + str(doc_id[i][1]) + ' ' + str(tmp) + ' ' + str(
            possible_answer[i]) + ' ' + str(all_rs[i]) + '\n'
        miss += 1
print(miss)
string += str(miss)
with open("result_find_answer_all.txt", "w", encoding="utf-8") as text_file:
    text_file.write(string)