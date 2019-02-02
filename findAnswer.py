import json

def extractNumberFromString(string):
    import re
    return re.findall('\d+', string )

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def make_sentence_answer(doc,answer_begin,n=15):
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

def order_consistency(index_a,index_b,l):
    return 1.0 - abs(index_a - index_b)/l

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี']
wrong = 949
all_rs = []
possible_answer = []
for i in range(wrong,a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']

    if answer.isnumeric():
        s = ''.join(question[i])
        print(i, s)
        question_index.append(i)
        real_answer.append([article_id,answer])
        doc = json.load(open('E:\CPE#Y4\databaseTF\documents-tokenize\\'+str(article_id)+'.json','r',encoding='utf-8-sig'))

        sentence_answer = make_sentence_answer(doc,answer_begin)
        doc_id.append([article_id])

        for j in question[i]:
            for w in question_words:
                if j.endswith(w) or j.startswith(w):
                    # s = s.replace(w,'')
                    for k in range(sentence_answer.__len__()):
                        if hasNumbers(sentence_answer[k]):
                            doc_id[-1].append(k)
                            # for num in extractNumberFromString(j):
                            #     question_index[-1].append(num)
                    break

        doc_id[-1][1:] = list(set(doc_id[-1][1:]))
        print(sentence_answer, doc_id[-1])
        if doc_id[-1].__len__() < 3:
            all_rs.append(1)
            possible_answer.append(sentence_answer[doc_id[-1][1]])
            doc_id[-1].insert(1, extractNumberFromString(sentence_answer[doc_id[-1][1]])[0])
            continue

        rs = []
        possible_answer.append([])
        for j in doc_id[-1][1:]:
            print(sentence_answer[j])
            possible_answer[-1].append(sentence_answer[j])
            score = []
            od = []
            for k in range(question[i].__len__()):
                tmp = ''.join(sentence_answer[j-k:j-k + question[i].__len__()])
                if not tmp :
                    continue
                od = []
                for l in range(question[i].__len__()):
                    try:
                        od.append(order_consistency(sentence_answer.index(question[i][l]), l, question[i].__len__()))
                    except ValueError:
                        od.append(0)
                print(normalized_edit_similarity(s, tmp),sum(od)/od.__len__())
                score.append(normalized_edit_similarity(s, tmp) + sum(od)/od.__len__())
            rs.append(max(score))
        print(rs)
        all_rs.append(rs)
        tmp_answer = extractNumberFromString(sentence_answer[doc_id[-1][rs.index(max(rs)) + 1]])
        doc_id[-1].insert(1,tmp_answer[0])
        exit(0)

print("Q:", doc_id.__len__(), real_answer.__len__())

string = ''
miss = 0
for i in range(real_answer.__len__()):
    if real_answer[i][1] != doc_id[i][1]:
        string += str(question_index[i]) + ' ' + str(real_answer[i]) + ' ' + str(doc_id[i][1]) + ' ' + str(possible_answer[i]) + ' ' + str(all_rs[i]) +'\n'
        miss+=1
print(miss)
string += str(miss)
with open("result_find_answer_word(1).txt", "a", encoding="utf-8") as text_file:
    text_file.write(string)
# TODO find the way to extract the answer from sentence
