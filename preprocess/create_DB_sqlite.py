from sqlitedict import SqliteDict
import os
import json
from pprint import pprint

def load_to_sqlite(path,files):
    for f in files:
        print(f)
        index = json.load(open(path + f, 'r', encoding='utf-8'))
        # print(index)
        delete = []
        for k, v in index.items():
            new = []
            tfidf = []
            for e in v:
                if e.__len__() > 4:
                    new.append([e[0], e[4]])
                    tfidf.append(e[4])

            try:
                new.insert(0, [sum(tfidf) / tfidf.__len__(), min(tfidf)])
                index[k] = new
            except:
                delete.append(k)
        for k in delete:
            del index[k]

        dict['doc'][f.replace('.json', '')] = index
doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\\new-db.sqlite', autocommit=True)

dict = {}
dict['doc'] = {}
path = 'E:\CPE#Y4\databaseTF\\new-dict-tfidf\\'
files = os.listdir(path)
files.remove("B_alphabet")

load_to_sqlite(path,files)

path = 'E:\CPE#Y4\databaseTF\\new-dict-tfidf\\B_alphabet\\'
files = os.listdir(path)

load_to_sqlite(path,files)

# print(dict)
doc['doc'] = dict
doc.commit()



