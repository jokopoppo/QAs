import json
from elasticsearch import Elasticsearch


def unique_items(L):
    found = []
    for item in L:
        if item not in found:
            found.append(item)

    return list(found)

def sentence_similar(a, b):
    a = set(a)
    b = set(b)

    return a.intersection(b).__len__() / a.union(b).__len__()


def sentences_in_doc(doc, over_lap, sen_len):
    sen = []
    for i in range(0, doc.__len__(), over_lap):
        if i + sen_len <= doc.__len__():
            tmp = doc[i:i + sen_len]
        else:
            tmp = doc[doc.__len__() - sen_len:]

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
validate_sentences = json.load(open("test_set\\validate_sentences_40.json", mode='r', encoding="utf-8-sig"))
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
n_doc = 2
for i in range(validate_doc.__len__()):
    sentence_rank = []
    for j in candidate_doc[i][:n_doc]:
        doc = query_doc_data(j)
        sentences = sentences_in_doc(doc, 20, 40)
        for k in sentences:
            scores = sentence_similar(k, q[i])
            sentence_rank.append([scores, j, k])

    sentence_rank.sort(key=lambda s: s[0], reverse=True)
    sentence_rank = unique_items(sentence_rank)

    sentence_rank = sentence_rank[:100]
    sentence_candidate.append(sentence_rank)
    acc += sentence_acc()

print(acc)
with open('E:\\CPE#Y4\\databaseTF\\sentence_candidate\\candidate_sen_2_doc_100rank_40len.json',
          'w', encoding="utf-8") as outfile:
    json.dump(sentence_candidate, outfile, ensure_ascii=False)
