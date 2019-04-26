import json
from elasticsearch import Elasticsearch


def sentence_similar(a, b):
    a = set(a)
    b = set(b)

    return a.intersection(b).__len__() / a.union(b).__len__()


def sentences_in_doc(doc):
    sen = []
    for i in range(0, doc.__len__(), 10):
        if i + 20 <= doc.__len__():
            tmp = doc[i:i + 20]
        else:
            tmp = doc[doc.__len__() - 20:]
        sen.append(tmp)
    return sen


def sentence_acc():
    for j in validate_sentences[i]:
        for k in sentence_rank:
            if j == k[2]:
                print(i, k)
                return 1
    return 0


def query_doc_data(doc_number):
    body = {
        "query": {
            "terms": {
                "_id": [doc_number]
            }
        }
    }
    res = es.search(index="index", doc_type="doc", body=body)
    for doc in res['hits']['hits']:
        if doc_number == doc["_id"]:
            return doc['_source']['text']
        else:
            print("ERROR doc_num does'nt match '_id'")
            exit()


q = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
validate_sentences = json.load(open("test_set\\validate_sentences.json", mode='r', encoding="utf-8-sig"))
candidate_doc = json.load(
    open("document_candidate/candidate_doc_ESsearch_w_text_boost3_q_no_space.json", mode='r', encoding="utf-8-sig"))

validate_answer = []
data = json.load(open('test_set/new_sample_questions.json', mode='r', encoding="utf-8-sig"))
for i in data['data']:
    validate_answer.append(i['answer'])

es = Elasticsearch()
path = 'E:\\CPE#Y4\\databaseTF\\new-documents-tokenize\\'
acc = 0

sentence_candidate = []
for i in range(candidate_doc.__len__()):
    sentence_rank = []
    for j in candidate_doc[i]:
        doc = query_doc_data(j)
        sentences = sentences_in_doc(doc)
        for k in sentences:
            scores = sentence_similar(k, q[i])
            sentence_rank.append([scores, validate_answer[i], k])

    sentence_rank.sort(key=lambda s: s[0], reverse=True)
    sentence_rank = sentence_rank[:100]
    sentence_candidate.append(sentence_rank)
    acc += sentence_acc()

print(acc)
with open('sentence_candidate\\candidate_sen_each_doc_100rank.json', 'w', encoding="utf-8") as outfile:
    json.dump(sentence_candidate, outfile, ensure_ascii=False)
