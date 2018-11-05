# coding=utf8
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)

from gensim.models import Word2Vec
import tensorflow as tf
from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize
import re
import numpy as np
import random

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

text_file = open("corpus/665.txt", encoding="utf8")
data = [text_file.read()]


data[0] = cleanhtml(data[0])
print("Raw  :",data)

tokendata=[list(word_tokenize(i,engine='newmm')) for i in data]
print("Tokenized    :",tokendata)
# model = Word2Vec(tokendata,size=3, min_count=1,window=5,sg=1)
# model.save('665txt-3d.bin')
modelW2V = Word2Vec.load("665txt-3d.bin")
words = list(modelW2V.wv.vocab)
print("Words    :",words)
dataTag=pos_tag(tokendata[0],engine='old')
print(dataTag)

nouns=[]
verbs=[]
adverbs=[]
prepo=[]

for _,x in dataTag:

    if (x=='NCMN' and _.__len__()>1 and _ not in nouns and nouns.__len__()<20):
        nouns.append((_,0))

    if (x == 'VACT' and _.__len__() > 1 and _ not in verbs and verbs.__len__()<20):
        verbs.append((_,1))

    if (x=='ADVN' and _.__len__()>1 and _ not in adverbs and adverbs.__len__()<20):
        adverbs.append((_,2))

    if (x == 'RPRE' and _.__len__() > 1 and _ not in prepo and prepo.__len__()<20):
        prepo.append((_,3))

train = [nouns,verbs,adverbs,prepo]
test = []
for i in train :
    for j in range(5):
        test.append(random.choice(i))
        i.remove(test[-1])

random.shuffle(train)
random.shuffle(test)

x_train = []
y_train =[]

x_test = []
y_test = []
for i in range(train.__len__()) :
    for j,_ in train[i]:
        x_train.append(modelW2V.wv[j])
        y_train.append(_)

for i,_ in test:
    x_test.append(modelW2V.wv[i])
    y_test.append(_)

x_train = np.asarray(x_train)
y_train = np.asarray(y_train)

x_test = np.asarray(x_test)
y_test = np.asarray(y_test)


# mnist = tf.keras.datasets.mnist # reference data
# (x_train, y_train),(x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0

modelPOS=tf.keras.models.load_model(
    "modelPOS_1000.h5",
    custom_objects=None,
    compile=True
)

# modelPOS = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(),
#   tf.keras.layers.Dense(512, activation=tf.nn.relu),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
# modelPOS.compile(optimizer='adam',
#                  loss='sparse_categorical_crossentropy',
#                  metrics=['accuracy'])
#
# modelPOS.fit(x_train, y_train, epochs=100)

test_loss, test_acc = modelPOS.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# tf.keras.models.save_model(
#     modelPOS,
#     "modelPOS.h5",
#     overwrite=True,
#     include_optimizer=True
# )