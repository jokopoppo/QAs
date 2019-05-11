from keras.models import Model
from keras.layers import Input, Dense, LSTM, RepeatVector, Concatenate, Bidirectional
from keras.utils import to_categorical
import numpy as np
from sklearn.metrics import confusion_matrix
import json


def init_word_vectors(words, word_vec, max_length=20):
    zero_vec = np.zeros(300)
    word_vectors = np.zeros((len(words), max_length, 300))

    for s in range(words.__len__()):
        for w in range(words[s].__len__()):
            try:
                word_vectors[s, w + (max_length - words[s].__len__()), :] = word_vec.wv[words[s][w]]
            except KeyError:
                word_vectors[s, w + (max_length - words[s].__len__()), :] = zero_vec
    return word_vectors


def init_test_set():
    from gensim.models import KeyedVectors
    word_vec_file = KeyedVectors.load_word2vec_format('E:\\CPE#Y4\\NLP\\wiki.th.vec')
    question = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
    sen = json.load(open('E:\\CPE#Y4\\databaseTF\\sentence_candidate\\candidate_sen_2_doc_100rank_40len.json', 'r',
                         encoding='utf-8-sig'))
    x1 = []
    x2 = []

    n = 0
    for i in sen:
        print(n, question[n])
        for j in i[:10]:
            x1.append(question[n])
            x2.append(j[2])
        n += 1
    print(len(x1), len(x2))

    return init_word_vectors(x1, word_vec_file, 40), init_word_vectors(x2, word_vec_file, 40)


def init_train_set(OUTPUT_CLASS=2):
    path = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
    x1_train = np.load(path + 'x1_train.npy')
    x2_train = np.load(path + 'x2_train.npy')
    y_test = np.load(path + 'y_train.npy')
    y_train = to_categorical(y_test, OUTPUT_CLASS)

    return x1_train, x2_train, y_train, y_test


def init_model():
    MAX_INPUT_LENGTH = 40
    INPUT_VECTOR_SIZE = 300
    LSTM_SIZE = 100
    MAX_OUTPUT_LENGTH = 40
    OUTPUT_CLASS = 2
    EMBEDED_OUTPUT_SIZE = 100

    inputEncoder = Input(shape=(MAX_INPUT_LENGTH, INPUT_VECTOR_SIZE,))
    encoder, hidden_state, cell_state = LSTM(LSTM_SIZE, activation='relu', return_state=True)(inputEncoder)

    quest_vec = RepeatVector(40)(encoder)

    inputDecoder = Input(shape=(MAX_OUTPUT_LENGTH, INPUT_VECTOR_SIZE,))
    concat = Concatenate(axis=2)([inputDecoder, quest_vec])
    dense = Dense(EMBEDED_OUTPUT_SIZE, activation='relu')(concat)

    decoder = LSTM(LSTM_SIZE, return_sequences=True)(dense, initial_state=[hidden_state, cell_state])
    outputLayer = Dense(OUTPUT_CLASS, activation='softmax')(decoder)

    model = Model(inputs=[inputEncoder, inputDecoder], outputs=outputLayer)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'],
                  )

    print(model.summary())

    return model


def init_Bidirectional_model():
    MAX_INPUT_LENGTH = 40
    INPUT_VECTOR_SIZE = 300
    LSTM_SIZE = 100
    MAX_OUTPUT_LENGTH = 40
    OUTPUT_CLASS = 2
    EMBEDED_OUTPUT_SIZE = 100

    inputEncoder = Input(shape=(MAX_INPUT_LENGTH, INPUT_VECTOR_SIZE,))
    encoder = Bidirectional(LSTM(LSTM_SIZE, activation='relu'))(inputEncoder)

    quest_vec = RepeatVector(40)(encoder)

    inputDecoder = Input(shape=(MAX_OUTPUT_LENGTH, INPUT_VECTOR_SIZE,))
    concat = Concatenate(axis=2)([inputDecoder, quest_vec])
    dense = Dense(EMBEDED_OUTPUT_SIZE, activation='relu')(concat)

    decoder = Bidirectional(LSTM(LSTM_SIZE, return_sequences=True))(dense)
    outputLayer = Dense(OUTPUT_CLASS, activation='softmax')(decoder)

    model = Model(inputs=[inputEncoder, inputDecoder], outputs=outputLayer)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'],
                  )

    print(model.summary())

    return model


def train_model():
    x1_train, x2_train, y_train, y_test = init_train_set()

    input_for_encoder = x1_train
    input_for_decoder = x2_train

    model = init_Bidirectional_model()
    model_name = 'extract_word_model_bidirectional.h5'
    model.load_weights(model_name)

    class_weight = [1, 20]
    model.fit([input_for_encoder, input_for_decoder], y_train, class_weight=class_weight, epochs=5, batch_size=100,
              validation_split=0.2)
    model.save('extract_word_model_bidirectional.h5')

    print('Predict')
    y_pred = model.predict([input_for_encoder[:, :, :], input_for_decoder[:, :, :]])

    y_pred = y_pred.argmax(axis=2)
    y_pred = y_pred.reshape((len(y_pred) * 40))
    #
    y_test = y_test.reshape((len(y_test) * 40))
    cm = confusion_matrix(y_test, y_pred)
    print('Confusion Matrix')
    print(cm)

def test_model():
    x1_train, x2_train = init_test_set()
    # x1_train, x2_train, y_train, y_test = init_train_set()
    print("Init test set")

    input_for_encoder = x1_train
    input_for_decoder = x2_train

    model = init_Bidirectional_model()
    model_name = 'extract_word_model_bidirectional.h5'
    model.load_weights(model_name)

    print('Predict')
    y_pred = model.predict([input_for_encoder[:, :, :], input_for_decoder[:, :, :]])
    np.save('y_pred_Bidirectional.npy', y_pred)

