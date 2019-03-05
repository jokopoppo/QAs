from keras.models import Model, Sequential
from keras.layers import Input, Dense, LSTM, Concatenate, Multiply, Subtract

sentence_length = 20
word_vector_length = 100


def sentenceVector():
    submodel = Sequential()
    submodel.add(LSTM(word_vector_length,activation='relu',input_shape=(sentence_length, word_vector_length, ),name='lstm'))
    return submodel

candidate_sentence_wv_seq = Input(shape=(sentence_length,word_vector_length,))
question_wv_seq = Input(shape=(sentence_length,word_vector_length,))

sv = sentenceVector()
candidate_sentence_sv = sv(candidate_sentence_wv_seq)
question_sv = sv(question_wv_seq)

diff = Subtract()([candidate_sentence_sv, question_sv])
squared_diff = Multiply()([diff, diff])
dissimilarity = Dense(1, activation='sigmoid', kernel_initializer='ones', bias_initializer='zeros', trainable=False)(squared_diff)

model = Model(inputs=[candidate_sentence_wv_seq, question_wv_seq], outputs=dissimilarity)

print(model.summary())

model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae','accuracy'])

model.save('model.h5')

sv_model = sentenceVector()
sv_model.load_weights('model.h5', by_name=True)
print(sv_model.summary())

