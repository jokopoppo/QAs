import json
import os
from elasticsearch import Elasticsearch

def es_index(es,start):
    path = 'E:\\CPE#Y4\\databaseTF\\new-documents-tokenize\\'
    files = os.listdir(path)

    for i in range(start, files.__len__()):
        data = json.load(open(path + files[i], 'r', encoding='utf-8'))

        doc = {
            'title': data[0],
            'text': data[1]
        }

        res = es.index(index="index", doc_type="doc", id=files[i].replace('.json', ''), body=doc)
        print(i, '/', files.__len__(), res['result'],files[i])

def search_index(question):
    content = ['text','title']
    query = []
    for k in range(content.__len__()):
        for i in question:
            boost = 1
            if k == 0:
                boost = 3
            q = {
                  "match": {
                    content[k]: {
                        "query": i,
                        "boost": boost
                    }
                  }
                }
            query.append(q)

    body = {
        "from": 0, "size": 10,
        "query": {
            "bool": {
              "should": query
            }
          }
    }
    res = es.search(index="index", doc_type="doc", body=body)
    # print("Got %d Hits:" % res['hits']['total'])

    doc_candidate = []
    for doc in res['hits']['hits']:
        doc_candidate.append(doc["_id"])
        # print(doc["_id"], doc['_source'])

    return doc_candidate







