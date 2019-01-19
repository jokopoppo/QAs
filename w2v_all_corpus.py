# coding=utf8

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)
from gensim.models import Word2Vec
import os
import json
import re
def cleadata(data_tokenize):

    data_tokenize.pop(0)
    data_tokenize.pop()
    for i in range(data_tokenize.__len__()):
        if data_tokenize[i].isnumeric():
            data_tokenize[i] = "NUM"
    return data_tokenize

datasets_dir = 'E:/CPE#Y4/databaseTF/documents-tokenize/'
datasets = os.listdir(datasets_dir)

model = Word2Vec.load("word2vec_model\word2vec.model")
print("Words in model",model.wv.vocab.__len__())

for i in range(110000,datasets.__len__()):
    # print(datasets[i])
    # exit(0)
    data = json.load(open(datasets_dir+datasets[i],'r',encoding='utf-8-sig'))
    data = cleadata(data)
    print("DOC",i,set(data).__len__(),end=" ")
    model.build_vocab([data],update=True)
    print(model.train([data], total_examples=1, epochs=1))

    if i%1000 == 0 :
        model.save("word2vec_model\word2vec.model")
        model = Word2Vec.load("word2vec_model\word2vec.model")
        print("Words in model", model.wv.vocab.__len__())

model.save("word2vec_model\word2vec.model")

# # test model
# ss=model.similar_by_word('พี่น้อง',topn=5)
# print(ss)

