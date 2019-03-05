from keras.models import Model, Sequential
from keras.layers import Input, Dense, LSTM, Concatenate, Multiply, Subtract,Bidirectional,Dropout,Lambda, RepeatVector,Flatten,Conv1D, Permute
from keras.backend import expand_dims,stack
import tensorflow as tf


question_length = 30
sentence_length = 20
word_vector_length = 100
compare_words_size = 32
word_score_size = 16


candidate_sentence_wv_seq = Input(shape=(sentence_length,word_vector_length,))
question_wv_seq = Input(shape=(question_length,word_vector_length,))


def compareWords():
    submodel = Sequential()
    submodel.add(Dense(compare_words_size,input_shape=(2*word_vector_length, )))
    submodel.add(Dense(compare_words_size))
    return submodel


candidate_sentence_split = Lambda(lambda x: tf.split(x, num_or_size_splits=sentence_length, axis=1))(candidate_sentence_wv_seq)
question_split = Lambda(lambda x: tf.split(x, num_or_size_splits=question_length, axis=1))(question_wv_seq)

cpw = compareWords()
for i in range(sentence_length):
    for j in range(question_length):
        temp = Concatenate()([candidate_sentence_split[i], question_split[j]])
        temp = cpw(temp)
        if(j == 0):
            candidate_word = temp
        else:
            candidate_word = Concatenate(axis=-1)([candidate_word,temp])
    word_score = Dense(word_score_size,activation='relu')((candidate_word))
    word_score = Dense(1, activation='relu')(word_score)
    if(i == 0):
        output = word_score
    else:
        output = Concatenate(axis=-1)([output, word_score])

output = Permute((2, 1))(output)
output = Conv1D(1,5,padding='same',activation='sigmoid')(output)

model = Model(inputs=[candidate_sentence_wv_seq, question_wv_seq], outputs=[output])

print(model.summary())

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['mae','accuracy'])



