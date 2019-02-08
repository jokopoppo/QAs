import json

def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

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

def check_question_type(a):

    c = a.split()
    n = a.count(' ')

    if n == 0:
        return c[0] in question[i]
    else:
        return c[1] in question[i] and question[i][question[i].index(c[1]) - n] == c[0]

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี' ,'ใคร' , 'ว่า' ,'อะไร']
classes = ['ใคร', 'ว่า อะไร', 'ประเทศ อะไร', 'จังหวัด อะไร', 'เมือง อะไร' , 'ประเทศ ใด', 'จังหวัด ใด', 'เมือง ใด' ,'คน ใด'
           , 'เมื่อ ใด', 'เวลา ใด', 'ภาค ใด', 'แคว้น ใด', 'ที่ ใด', 'ที่ ไหน', 'เท่า ไร', 'เมื่อ ไร', 'อย่าง ไร', 'ชื่อ อะไร', 'ปี อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'other ใด', 'other อะไร']
# 145 questions cant find question word because token words are not good enough .
question_type = [['กี่', 'ปี ใด', 'ปี อะไร', 'พ.ศ.  อะไร', 'ค.ศ.  อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'พ.ศ. ใด', 'พ.ศ.  ใด', 'ค.ศ. ใด', 'ค.ศ.  ใด', 'เท่า ไร', 'เท่า ไหร่', 'เท่า ใด' ,'คริสต์ศักราช ใด', 'จำนวน ใด']
                 , ['เมื่อ ไร', 'เวลา ใด', 'วัน ใด' ,'เมื่อ ใด', 'วัน ที่'] # date format
                 , ['ใคร', 'ว่า อะไร', 'ชื่อ อะไร', 'คน ใด', 'คน ไหน', 'คือใคร', 'ผู้ ใด'] # human name
                 , ['ประเทศ ใด', 'ประเทศ อะไร']
                 , ['จังหวัดใด','จังหวัด ใด', 'จังหวัด อะไร']
                 , ['เมืองใด','เมือง ใด', 'เมือง อะไร']
                 , ['ภาค ใด']
                 , ['แคว้น ใด']
                 , ['ทวีปใด', 'ทวีป อะไร', 'ทวีป ใด', 'ภูมิภาค ไหน']
                 , ['ที่ ไหน', 'ที่ ใด'] # where
                 , ['อะไร', 'อย่าง ไร', 'ใด', 'ไหน'] # other what, other dai, other nhai
                  ]

wrong = 0
all_rs = []
possible_answer = []

n = 0
ans = []
s_ans = []
wv = []

for i in range(wrong,a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']
    sentence_answer = make_sentence_answer(article_id, answer_begin)

    for l in range(question_type.__len__()):
        if any(check_question_type(k) for k in question_type[l]):
            if l != 11:
                # print(l,i,answer,question[i])
                # print(sentence_answer)
                n+=1

                ans.append([l, answer])
                s_ans.append(sentence_answer)
                wv.append([])
                for j in sentence_answer:
                    if (j in answer) and (j.__len__() >= 2):
                        wv[-1].append(j)
            break

        elif l == 10 and not any(check_question_type(k) for k in question_type[l]):
            # print(l,i,answer,question[i])
            n+=1

            ans.append([l, answer])
            s_ans.append(sentence_answer)
            wv.append([])
            for j in sentence_answer:
                if (j in answer) and (j.__len__() >= 2):
                    wv[-1].append(j)

print(n)

miss = 0
count = 0
string = ''
lab = [6,7,8,9,10]

for label in lab:
    for i in range(ans.__len__()):
        if ans[i][0] == label:
            if wv[i].__len__() < 1:
                for j in s_ans[i]:
                    d = similar(j, ans[i][1])
                    if d > 0.45:
                        wv[i].append(j)

                if wv[i].__len__() < 1:
                    miss += 1
                print(ans[i], wv[i], s_ans[i])
                count += 1
                string += str(wv[i]) + '\n'
            else:
                print(ans[i], wv[i], s_ans[i])
                count += 1
                string += str(wv[i]) + '\n'

    print(count, miss)
    with open("train_set_for_classify//" + str(label) + ".txt", "w", encoding="utf-8") as text_file:
        text_file.write(string)
