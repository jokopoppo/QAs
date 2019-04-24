import json

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

def sentence_similar(a, b):
    a = set(a)
    b = set(b)

    return a.intersection(b).__len__() / a.union(b).__len__()


def make_validate_sentences(validate_doc, validate_answer, answer_position):
    path = 'E:\\CPE#Y4\\databaseTF\\new-documents-tokenize\\'
    validate_sentences = []
    for i in range(validate_doc.__len__()):
        validate_sentences.append([])
        print(i,validate_answer[i],validate_doc[i])
        doc = json.load(open(path + str(validate_doc[i]) + '.json', mode='r', encoding="utf-8-sig"))[1]
        # print(doc)
        for j in range(0,doc.__len__(), 10):
            if j+20 <= doc.__len__():
                tmp = doc[j:j+20]
            else:
                tmp = doc[doc.__len__()-20:]

            for k in tmp:
                if similar(validate_answer[i], k) > 0.4:
                    validate_sentences[-1].append(tmp)
                    break
                elif k.endswith(validate_answer[i]) or validate_answer[i].endswith(k) or k in validate_answer[i]:
                    validate_sentences[-1].append(tmp)
                    break
            if validate_sentences[-1].__len__() > 1:
                break
        # print(validate_sentences[-1])
        if validate_sentences[-1].__len__() < 1:
            print(doc)
            break
    with open('test_set\\validate_sentences.json', 'w',
              encoding="utf-8") as outfile:
        json.dump(validate_sentences, outfile, ensure_ascii=False)

def compare2sentence():

validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
data = json.load(open('test_set/new_sample_questions.json', mode='r', encoding="utf-8-sig"))
q = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
validate_answer = []
answer_position = []
for i in data['data']:
    validate_answer.append(i['answer'])
print(validate_answer)

# make_validate_sentences(validate_doc, validate_answer, answer_position)

