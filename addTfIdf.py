from sklearn.feature_extraction.text import TfidfVectorizer
# import deepcut
import re
import json
import pickle
from pprint import pprint
import os
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

dataset_path = "E:\CPE#Y4\databaseTF\documents-tokenize\\"
datasets = os.listdir(dataset_path)

files = []
for dataset in datasets:
    if(dataset == 'test.txt'):
        break
    files.append(int((dataset.split("."))[0]))

files = sorted(files)
print(files.__len__())
# s=[]

# for f in files :
#     file = open(dataset_path + str(f) + '.json', mode = 'r' , encoding="utf-8-sig")
#     s.append(json.load(file))
#     print(f)
#
# print(s.__len__())

# TODO fix this to open all index files and run this after indexing done

def dummy_fun(doc):
    return doc

# tfidf = TfidfVectorizer(
#
#     tokenizer=dummy_fun,
#     preprocessor=dummy_fun,
#     token_pattern=None)


tfidf = pickle.load(open("tfidf.pickle", "rb" ) )
response = pickle.load(open("response.pickle", "rb" ) )
feature_names = tfidf.get_feature_names()
print(feature_names.__len__())

print("open")

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# TODO run this shit for add tfidf

dictset = [alphabet,e_alphabet]
for d in dictset:
    alp=[]
    for i in d:
        alp.append({})
    print(alp.__len__())

    for doc in range(files.__len__()):
        print(doc)
        feature_index = response[doc,:].nonzero()[1]
        tfidf_scores = zip(feature_index, [response[doc, x] for x in feature_index])

        for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
            # print(doc,w,s)
            if(w[0] in d):
                tmp = d.index(w[0])
                if (alp[tmp].get(w) is None):
                    alp[tmp][w] = []
                alp[tmp][w] = s
                # print(w,alp[tmp][w])

    dict_path = 'E:\CPE#Y4\databaseTF\dict2\\'
    for i in range(alp.__len__()):
        filename = dict_path + str(d[i]) + ".json"
        print(filename)
        data = json.load(open(filename))

        for k,v in alp[i].items():
            if(data.get(k) != None):
                data[k][0].append(v)


        json.dump(data,open(filename,'w'), ensure_ascii=True)