from sklearn.feature_extraction.text import TfidfVectorizer
# import deepcut
import re
import json
import pickle
from pprint import pprint
import os
import time


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


start = time.time()
dataset_path = "E:\CPE#Y4\databaseTF\\new-documents-tokenize\\"
datasets = os.listdir(dataset_path)

files = []
for dataset in datasets:
    files.append(int((dataset.split("."))[0]))

# files = sorted(files)
print(files.__len__())

def dummy_fun(doc):
    return doc


# tfidf = TfidfVectorizer(
#
#     tokenizer=dummy_fun,
#     preprocessor=dummy_fun,
#     token_pattern=None)

dir = 'E:\CPE#Y4\databaseTF\\tf-idf_model\\'
tfidf = pickle.load(open(dir + "tfidf.pickle", "rb"))
response = pickle.load(open(dir + "response.pickle", "rb"))
feature_names = tfidf.get_feature_names()
print(feature_names.__len__())

print("open")

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
be_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
dictset = [be_alphabet] # TODO change dictset and run this
for d in dictset:
    alp = []
    for i in d:
        alp.append({})
    print("alp", alp.__len__())

    for doc in range(files.__len__()):
        print(doc)
        feature_index = response[doc, :].nonzero()[1]
        tfidf_scores = zip(feature_index, [response[doc, x] for x in feature_index])

        for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
            # print(doc,w,s)

            if not w:
                continue
            if (w[0] in d):
                tmp = d.index(w[0])
                if (alp[tmp].get(w) is None):
                    alp[tmp][w] = []
                alp[tmp][w].append([files[doc], s])
        # if doc == 1 : ## if bug fix it here
        #     break
    # pprint(alp)
    dict_path = 'E:\CPE#Y4\databaseTF\\new-dict\\'
    save_path = 'E:\CPE#Y4\databaseTF\\new-dict-tfidf\\'
    for i in range(alp.__len__()):
        filename = dict_path + str(d[i]) + ".json"
        print(filename)
        data = json.load(open(filename))
        count = alp[i].__len__()
        for k, v in alp[i].items():
            # count-=1
            # print(count)
            # print(k,v)
            # print(data.get(k)) ## if bug fix it here
            if (data.get(k) != None):
                for j in range(data[k].__len__()):
                    if int(data[k][j][0]) == v[0][0]:
                        if data[k][j].__len__() != 5:
                            data[k][j].append(v[0][1])
                            v.remove(v[0])
                            if v:
                                continue
                            else:
                                break
                        else:
                            data[k][j][4] = v[0][1]
                            v.remove(v[0])
                            if v:
                                continue
                            else:
                                break

        print('Dump !!')
        json.dump(data, open(save_path + str(d[i]) + ".json", 'w', encoding='utf-8'), ensure_ascii=False)

end = time.time()
print(end - start)
