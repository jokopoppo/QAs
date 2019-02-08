import tensorflow as tf
from tensorflow import keras
import numpy as np

x_train, y_train = np.load('train_set_for_classify/x_train.npy'), np.load('train_set_for_classify/y_train.npy')
for i in range(y_train.__len__()):
    y_train[i] -= 2
print(x_train.shape,y_train.shape,y_train)

model = keras.Sequential([
    keras.layers.Dense(100, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50)

# tf.keras.models.save_model(
#     model,
#     'classify_model.hdf5',
#     overwrite=True,
#     include_optimizer=True
# )

