# coding=utf8

from pythainlp.corpus import stopwords
from ast import literal_eval
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)
from gensim.models import Word2Vec
import numpy as np

stop_words = stopwords.words('thai')
stop_words.append('กี่')
stop_words.append('ใด')

model = Word2Vec.load("E:\CPE#Y4\databaseTF\word2vec_model_lastest\word2vec.model")

lab = [2, 3, 4, 5, 6, 7, 8, 9, 10]
x_train = []
y_train = []
for label in lab:
    data = open("train_set_for_classify//" + str(label) + ".txt", "r", encoding="utf-8")
    for i in data:
        i = [j for j in literal_eval(i)]
        print(i)
        for j in i:
            try:
                print(label, j)
                x_train.append(model.wv[j])
                y_train.append(label)
            except KeyError:
                print("###############",label,j)
                continue

label = 11
for j in stop_words:
    try:
        print(label, j)
        x_train.append(model.wv[j])
        y_train.append(label)
    except KeyError:
        print("###############", label, j)
        continue

x_train = np.asarray(x_train)
y_train = np.asarray(y_train)

np.save('train_set_for_classify/x_train.npy', x_train)
np.save('train_set_for_classify/y_train.npy', y_train)
