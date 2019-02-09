import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import save_model, load_model

x_train, y_train = np.load('train_set_for_classify/x_train.npy'), np.load('train_set_for_classify/y_train.npy')
for i in range(y_train.__len__()):
    y_train[i] -= 2
print(x_train.shape,y_train.shape,y_train)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(100, )),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# model = tf.keras.models.load_model(
#     'model.h5py',
#     custom_objects=None,
#     compile=True
# )

model.fit(x_train, y_train, epochs=100)

model.save('model.h5py')


