import tensorflow as tf
from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize

data="ฉันรักเธอ"
data=word_tokenize(data,engine='newmm')
data=pos_tag(data,engine='old')
print(data)
# mnist = tf.keras.datasets.mnist

# (x_train, y_train),(x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
#
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(),
#   tf.keras.layers.Dense(512, activation=tf.nn.relu),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(x_train, y_train, epochs=1)
# model.evaluate(x_test, y_test)