from sklearn.feature_extraction.text import TfidfVectorizer
import os
import json
import pickle
def dummy_fun(doc):
    return doc
tfidf = TfidfVectorizer(

    tokenizer=dummy_fun,
    preprocessor=dummy_fun,
    token_pattern=None)

corpus = []
path = "E:\CPE#Y4\databaseTF\\new-documents-tokenize\\"
files = os.listdir(path)

for i in range(files.__len__()):
    print(i)
    doc = json.load(open(path + str(files[i]),'r',encoding='utf-8'))
    corpus.append(doc[1])

response = tfidf.fit_transform(corpus)
feature_names = tfidf.get_feature_names()
print(feature_names.__len__())

with open("E:\CPE#Y4\databaseTF\\tf-idf_model\\response.pickle", 'wb') as pickle_file:
    pickle.dump(response,pickle_file, pickle.HIGHEST_PROTOCOL)
with open("E:\CPE#Y4\databaseTF\\tf-idf_model\\tfidf.pickle", 'wb') as pickle_file:
    pickle.dump(tfidf,pickle_file, pickle.HIGHEST_PROTOCOL)
