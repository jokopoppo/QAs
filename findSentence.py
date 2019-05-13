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



