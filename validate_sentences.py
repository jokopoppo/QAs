import json


def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()


def sentence_similar(a, b):
    a = set(a)
    b = set(b)

    return a.intersection(b).__len__() / a.union(b).__len__()


def make_validate_sentences(validate_doc, validate_answer, answer_postition, overlap, sen_len):
    path = 'E:\\CPE#Y4\\databaseTF\\new-documents-tokenize\\'
    validate_sentences = []
    for i in range(validate_doc.__len__()):
        validate_sentences.append([])
        doc = json.load(open(path + str(validate_doc[i]) + '.json', mode='r', encoding="utf-8-sig"))[1]
        # print(doc)
        print(i, validate_answer[i])
        pos = 0
        answer_idx = 0
        for j in range(0, doc.__len__(), 1):
            pos += doc[j].__len__()
            if pos > answer_postition[i][0]:
                answer_idx = j
                break
        for j in range(0, doc.__len__(), overlap):
            if j + sen_len <= doc.__len__():
                tmp = doc[j:j + sen_len]
            else:
                tmp = doc[doc.__len__() - sen_len:]

            if j <= answer_idx < j + sen_len:
                validate_sentences[-1].append(tmp)
            if validate_sentences[-1].__len__() > 2:
                print(validate_sentences[-1])
                break

        if validate_sentences[-1].__len__() < 1:
            print("ERROR no validate sentence")
            print(doc)
            break
    with open('test_set\\validate_sentences_40.json', 'w', encoding="utf-8") as outfile:
        json.dump(validate_sentences, outfile, ensure_ascii=False)


validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
q = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))

validate_answer = []
answer_postition = json.load(open('test_set/new_answer_positions.json', mode='r', encoding="utf-8-sig"))
print(answer_postition.__len__())
data = json.load(open('test_set/new_sample_questions.json', mode='r', encoding="utf-8-sig"))
for i in data['data']:
    validate_answer.append(i['answer'])
# print(validate_answer)

make_validate_sentences(validate_doc, validate_answer, answer_postition, 20, 40)
