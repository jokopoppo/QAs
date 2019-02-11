import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import save_model, load_model
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)
from gensim.models import Word2Vec
import json
# x_train, y_train = np.load('train_set_for_classify/x_train.npy'), np.load('train_set_for_classify/y_train.npy')
# for i in range(y_train.__len__()):
#     y_train[i] -= 2
# print(x_train.shape,y_train.shape,y_train)

# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(100, )),
#     keras.layers.Dense(512, activation=tf.nn.relu),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dropout(0.2),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
wv_model = Word2Vec.load("E:\CPE#Y4\databaseTF\word2vec_model_lastest\word2vec.model")

model = tf.keras.models.load_model(
    'model.h5py',
    custom_objects=None,
    compile=True
)
wv = []
words = []
for word in wv_model.wv.vocab:
    print(word)
    words.append(word)
    wv.append(wv_model.wv[word])

label = []
wv = np.asarray(wv)
predictions = model.predict(wv)

file = []
for i in range(2,12):
    file.append([])
for i in range(predictions.__len__()):
    tmp = np.argmax(predictions[i])
    file[tmp].append(words[i])

add2 = json.load(open('word_class\\Winner_Boss\\'  + '2.json', 'r', encoding="utf-8"))
add9 = json.load(open('word_class\\Winner_Boss\\'  + '9.json', 'r', encoding="utf-8"))
add10 = json.load(open('word_class\\Winner_Boss\\'  + '10.json', 'r', encoding="utf-8"))

for i in add2:
    file[0].append(i)
for i in add9:
    file[7].append(i)
for i in add10:
    file[8].append(i)

for i in range(file.__len__()):
    with open('word_class\\' + str(i+2) + '.json', 'w', encoding="utf-8") as outfile:
        json.dump(file[i], outfile, indent=4, ensure_ascii=False)

# model.fit(x_train, y_train, epochs=100)

# model.save('model.h5py')


