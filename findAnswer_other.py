import json

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี' ]
wrong = 0
all_rs = []
possible_answer = []

n = 0
for i in range(wrong,a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']

    if hasNumbers(answer):
        print(i , answer ,question[i])
        n+=1
print(n)