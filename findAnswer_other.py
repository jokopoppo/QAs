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

def check_question_type(a,b,n):
    return b in question[i] and question[i][question[i].index(b) - n] == a

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี' ,'ใคร' , 'ว่า' ,'อะไร']
classes = ['number', 'กี่', 'ใคร', 'ว่า อะไร', 'ประเทศ อะไร', 'จังหวัด อะไร', 'เมือง อะไร' , 'ประเทศ ใด', 'จังหวัด ใด', 'เมือง ใด' ,'คน ใด'
           , 'เมื่อ ใด', 'เวลา ใด', 'ภาค ใด', 'แคว้น ใด', 'ที่ ใด', 'ที่ ไหน', 'เท่า ไร', 'เมื่อ ไร', 'อย่าง ไร', 'ชื่อ อะไร', 'other ใด', 'other อะไร']
# 145 questions cant find question word because token words are not good enough .
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

    if not answer.isnumeric() and 'ใคร' not in question[i] and 'ไร' not in question[i]\
            and 'กี่' not in question[i] and 'อะไร' not in question[i] and 'ใด' not in question[i]\
            and not check_question_type('ประเทศ','ใด',1) \
            and not check_question_type('จังหวัด', 'ใด',1) \
            and not check_question_type('เมือง', 'ใด',1) \
            and not check_question_type('คน', 'ใด',1) \
            and not check_question_type('ปี', 'ใด', 1) \
            and not check_question_type('พ.ศ.', 'ใด', 2) \
            and not check_question_type('ค.ศ.', 'ใด', 2)\
            and not check_question_type('เมื่อ','ใด',1) \
            and not check_question_type('เวลา', 'ใด', 1) \
            and not check_question_type('ภาค', 'ใด', 1) \
            and not check_question_type('แคว้น', 'ใด', 1) \
            and not check_question_type('ที่', 'ใด', 1) \
            and not check_question_type('ที่','ไหน', 1):

            print(i,answer,question[i])
        #   print(sentence_answer)
            n+=1
            ans.append([i, answer])
            s_ans.append(sentence_answer)
            wv.append([])
            for j in sentence_answer:
                if (j in answer) and (j.__len__() >= 2):
                    wv[-1].append(j)

print(n)

# count = 0
# string = ''
# for i in range(ans.__len__()):
#     if wv[i].__len__() > 0 :
#         # for j in s_ans[i]:
#         #     d = similar(j,ans[i][1])
#         #     if d > 0.55:
#         #         wv[i].append(j)
#         print(ans[i],wv[i],s_ans[i])
#         count+=1
#         string += str(wv[i]) + '\n'
# print(count)
# with open("train_set_for_classify/ที่ไหน.txt", "a", encoding="utf-8") as text_file:
#     text_file.write(string)
