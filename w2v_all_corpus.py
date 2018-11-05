# coding=utf8
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)

from gensim.models import Word2Vec
from pythainlp.tokenize import word_tokenize , sent_tokenize

import re
import os
import deepcut

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

path = 'D:/CPE#Y4/documents-nsc/'
datasets = os.listdir(path)
# print(datasets.__len__())
fs = []
for dataset in datasets:
    if(dataset == 'test.txt'):
        break
    fs.append(int((dataset.split("."))[0]))

fs = sorted(fs)

data=[]
count = 0
for i in range(19000,20000):

    text_file = open(path+ str(fs[i]) + '.txt', mode = 'r' ,  encoding="utf-8")
    data.append(text_file.read())
    data[-1]=cleanhtml(data[-1])

    if(i%100 == 0 or i == (fs.__len__() - 1 )):
        print(i,count)
        count+=1
        print("#readed_file", data.__len__())

        tokendata = [list(deepcut.tokenize(i)) for i in data]

        print("Start training")
        # model = Word2Vec(tokendata, min_count=1,window=5,sg=1)
        model = Word2Vec.load("w2v_all_corpus.bin")

        words = list(model.wv.vocab)
        print("Words    :", words.__len__())

        model.build_vocab(tokendata, update=True)
        model.train(tokendata, total_examples=1, epochs=1)

        words = list(model.wv.vocab)
        print("Words    :", words.__len__())

        model.save('w2v_all_corpus.bin')
        data=[]

# test model
# ss=model.similar_by_word('พี่น้อง',topn=5)
# print(ss)


