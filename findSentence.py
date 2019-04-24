import json

def sentence_similar(a, b):
    a = set(a)
    b = set(b)

    return a.intersection(b).__len__() / a.union(b).__len__()


validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
data = json.load(open('test_set\\new_sample_questions.json', mode='r', encoding="utf-8-sig"))
q = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
validate_answer = []
answer_position = []
for i in data['data']:
    validate_answer.append(i['answer'])
    answer_position.append(i["answer_begin_position "])
print(validate_answer)




