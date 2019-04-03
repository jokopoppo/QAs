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

    query = []
    for i in question:
        q = {
                  "match": {
                    "text": i
                  }
                }
        query.append(q)

    body = {
        "query": {
            "bool": {
              "should": query
            }
          }
    }
    res = es.search(index="index", doc_type="doc", body=body)
    print("Got %d Hits:" % res['hits']['total'])
    for doc in res['hits']['hits']:
        print(doc["_id"],doc['_source']['title'])

es = Elasticsearch()

es_index(es,35777)
# q = json.load(open('test_set\\new_sample_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
#
# search_index(q[0])





