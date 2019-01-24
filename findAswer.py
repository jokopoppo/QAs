import json

def answer_word(doc,answer_begin,answer_end):
    word = ''
    for i in range(answer_begin - 1, answer_end):
        word +=doc[i]
    return word

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']

q = []
for i in range(a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']

    if hasNumbers(answer):
        q.append([i,answer])
        print(i,answer)
    # doc = open('E:\CPE#Y4\databaseTF\documents-nsc\\'+str(article_id)+'.txt','r',encoding='utf-8-sig')
    # for i in doc:
    #     doc = i
    # print(doc)

print(q.__len__())

# TODO find the way to extract the answer from sentence
