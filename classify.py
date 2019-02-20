import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import save_model, load_model
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)
from gensim.models import Word2Vec
import json

def reformatXY(x_train,y_train):
    w = [3, 4, 5, 6, 7, 8, 9]
    for i in range(y_train.__len__()):
        print(y_train[i])
        if y_train[i] in w:
            y_train[i] = 3
        elif y_train[i] == 10:
            y_train[i] = 4
        elif y_train[i] == 11:
            y_train[i] = 5
        y_train[i] -= 2
    return x_train,y_train

def init_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(100,)),
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(128, activation=tf.nn.sigmoid),
        keras.layers.Dense(128, activation=tf.nn.tanh),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

def tag_corpus(model):
    wv_model = Word2Vec.load("E:\CPE#Y4\databaseTF\word2vec_model_lastest\word2vec.model")
    wv = []
    words = []
    for word in wv_model.wv.vocab:
        print(word)
        words.append(word)
        wv.append(wv_model.wv[word])

    wv = np.asarray(wv)
    predictions = model.predict(wv)

    file = []
    for i in range(2, 6):
        file.append([])
    for i in range(predictions.__len__()):
        tmp = np.argmax(predictions[i])
        file[tmp].append(words[i])

    for i in range(file.__len__()):
        with open('word_class\\' + str(i + 2) + '.json', 'w', encoding="utf-8") as outfile:
            json.dump(file[i], outfile, indent=4, ensure_ascii=False)

x_train, y_train = np.load('train_set_for_classify/x_train.npy'), np.load('train_set_for_classify/y_train.npy')
x_train, y_train = reformatXY(x_train,y_train)
print(x_train.shape, y_train.shape, y_train)

# model = init_model()

model = tf.keras.models.load_model(
    'model.h5py',
    custom_objects=None,
    compile=True
)

tag_corpus(model)

# model.fit(x_train, y_train, epochs=100)
# model.save('model.h5py')


