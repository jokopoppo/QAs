from keras.models import Model
from keras.layers import Input, Dense, LSTM
from keras.utils import to_categorical
import numpy as np
from sklearn.metrics import confusion_matrix


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

    inputDecoder = Input(shape=(MAX_OUTPUT_LENGTH, INPUT_VECTOR_SIZE,))
    dense = Dense(EMBEDED_OUTPUT_SIZE, activation='relu')(inputDecoder)
    decoder = LSTM(LSTM_SIZE, return_sequences=True)(dense, initial_state=[hidden_state, cell_state])
    outputLayer = Dense(OUTPUT_CLASS, activation='softmax')(decoder)

    model = Model(inputs=[inputEncoder, inputDecoder], outputs=outputLayer)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'],
                  )

    print(model.summary())

    return model


x1_train, x2_train, y_train, y_test = init_train_set()
input_for_encoder = x1_train
input_for_decoder = x2_train

model = init_model()
model_name = 'extract_word_model.h5'
model.load_weights(model_name)

# class_weight = [1, 20]
# model.fit([input_for_encoder, input_for_decoder], y_train,class_weight=class_weight, epochs=1, batch_size=100,
#           validation_split=0.2)
# model.save('extract_word_model.h5')

# length = int(y_train.__len__() * 20 / 100)
y_pred = model.predict([input_for_encoder[:, :, :], input_for_decoder[:, :, :]])
np.save('y_pred.npy',y_pred)

y_test = y_test.reshape((len(y_test) * 40))

y_pred  = y_pred.argmax(axis=2)
y_pred = y_pred.reshape((len(y_pred) * 40))

cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix')
print(cm)

## TODO test this shit
