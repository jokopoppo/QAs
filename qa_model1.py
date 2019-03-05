from keras.models import Model, Sequential
from keras.layers import Input, Dense, LSTM, Concatenate, Multiply, Subtract,Bidirectional,Dropout,Lambda, RepeatVector
import tensorflow as tf


question_length = 30
sentence_length = 20
word_vector_length = 100
lstm_size = int(word_vector_length/2)


candidate_sentence_wv_seq = Input(shape=(sentence_length,word_vector_length,))
question_wv_seq = Input(shape=(question_length,word_vector_length,))

question_sv = Bidirectional(LSTM(lstm_size, activation='relu'))(question_wv_seq)
question_sv = Dropout(0.5)(question_sv)

candidate_sentence_lstm = Bidirectional(LSTM(lstm_size, activation='relu', return_sequences=True))(candidate_sentence_wv_seq)
candidate_sentence_lstm = Dropout(0.5)(candidate_sentence_lstm)

def sentenceDissimlarity():
    input1 = Input(shape=(2*lstm_size,))
    input2 = Input(shape=(sentence_length, 2*lstm_size,))
    split = Lambda(lambda x: tf.split(x, num_or_size_splits=sentence_length, axis=1))(input2)
    diff = Subtract()([input1, split[sentence_length-1]])
    squared_diff = Multiply()([diff, diff])
    dissimilarity = Dense(1, activation='sigmoid', kernel_initializer='ones', bias_initializer='zeros',trainable=False)(squared_diff)
    submodel = Model(inputs=[input1, input2],outputs=dissimilarity)
    return submodel

def answerProbability():
    input1 = Input(shape=(2*lstm_size,))
    input2 = Input(shape=(sentence_length, 2*lstm_size,))
    input1_rep = RepeatVector(sentence_length)(input1)
    concat = Concatenate(axis = -1)([input1_rep, input2])
    lstm = Bidirectional(LSTM(lstm_size, activation='relu', return_sequences=True))(concat)
    lstm = Dropout(0.5)(lstm)
    ansprob = Dense(1,activation='sigmoid')(lstm)
    submodel = Model(inputs=[input1, input2],outputs=ansprob)
    return submodel

dissimilarity = sentenceDissimlarity()([question_sv, candidate_sentence_lstm])
ansProb = answerProbability()([question_sv, candidate_sentence_lstm])

model = Model(inputs=[candidate_sentence_wv_seq, question_wv_seq], outputs=[dissimilarity, ansProb])

print(model.summary())
