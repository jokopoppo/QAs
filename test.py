import numpy as np
from keras.utils import to_categorical

path2 = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
y_train = np.load(path2 + 'y_train.npy')
y_pred = np.load('y_pred.npy')

y_pred = y_pred.reshape((4000,5,40))
y_train = y_train.reshape((4000,5,40))

mrr = []
for i in range(len(y_train)):
    for j in range(len(y_train[i])):
        if np.array_equal(y_train[i][j], y_pred[i][j]):
            mrr.append(j)
            break
print(mrr.__len__())
print(mrr)

score = 0
for i in mrr:
    score+=1/(i+1)

print(score/4000)