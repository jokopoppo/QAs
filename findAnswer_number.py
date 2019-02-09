import json

def extractNumberFromString(string):
    import re
    return re.findall('\d+', string )

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def make_sentence_answer(article_id,answer_begin,n=15):
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

def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

def relevance_score(question,sentence,candidate,question_word):

    a = []
    question_word_index = question.index(question_word)
    l = 2*question.__len__()
    for i in candidate :
        a.append([])
        for j in range(i-l,i+l):
            if (i != j) and (0 <= j < sentence.__len__()) and (sentence[j] in question):
                if question.index(sentence[j]) < question_word_index:
                    a[-1].append([question.index(sentence[j]), j, 0.5])
                else:
                    a[-1].append([question.index(sentence[j]), j, 0.25])
        # print(a[-1])

    m = question.__len__() - 1

    score = []
    for i in range(a.__len__()) :
        tmp = 0
        for j in a[i]:
            tmp += (1-abs(j[1] - candidate[i])/l)*(1 - abs(j[0] - question_word_index)/m )
        score.append(tmp)

    return score

def find_question_word(question,doc_id):
    for j in question:
        for w in question_words:
            if j.endswith(w) or j.startswith(w):
                if j.endswith('ปี'):
                    continue
                for k in range(sentence_answer.__len__()):
                    if hasNumbers(sentence_answer[k]):
                        doc_id.append(k)
                return [question.index(j), j],doc_id

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'ใด', 'เท่า', 'ปี', 'อะไร']
wrong = 0
all_rs = []
possible_answer = []
for i in range(wrong,a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']

    if answer.isnumeric():
        s = ''.join(question[i])
        question_index.append(i)
        real_answer.append([article_id,answer])

        sentence_answer = make_sentence_answer(article_id,answer_begin)
        doc_id.append([article_id])

        question_word_index,doc_id[-1] = find_question_word(question[i],doc_id[-1])

        possible_answer.append([])
        for j in doc_id[-1][1:]:
            possible_answer[-1].append(sentence_answer[j])

        print(i, s)
        print(possible_answer[-1])
        print(question_word_index,question[i])
        print(sentence_answer, doc_id[-1])

        score = relevance_score(question[i], sentence_answer, doc_id[-1][1:], question_word_index[1])
        all_rs.append(score)
        doc_id[-1].insert(1,extractNumberFromString(sentence_answer[doc_id[-1][score.index(max(score)) + 1]]))
        print(score)

        if score.__len__() > 1:
            exit(0)
print("Q:", doc_id.__len__(), real_answer.__len__())

# string = ''
# miss = 0
# for i in range(real_answer.__len__()):
#
#     if real_answer[i][1] != doc_id[i][1][0]:
#         string += str(question_index[i]) + ' ' + str(real_answer[i]) + ' ' + str(doc_id[i][1][0]) + ' ' + str(possible_answer[i]) + ' ' + str(all_rs[i]) +'\n'
#         miss+=1
# print(miss)
# string += str(miss)
# with open("result_find_answer_word_number(1).txt", "w", encoding="utf-8") as text_file:
#     text_file.write(string)
