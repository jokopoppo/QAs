import os
import json
import numpy as np
from gensim.models import KeyedVectors


def save_data_for_extract_answer():
    path = 'train_set_for_classify/positive_sentences/'
    file = os.listdir(path)
    question = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
    x2_train = []
    x1_train = []
    y_train = []
    for i in range(file.__len__()):
        data = json.load(open(path + file[i], 'r', encoding='utf-8-sig'))
        for j in data:
            y_train.append(j['sample_answer_maks'])
            x2_train.append(j['sample_sentence'])
            x1_train.append(question[i])

    with open('train_set_for_classify/x1.json', 'w', encoding="utf-8") as outfile:
        json.dump(x1_train, outfile, ensure_ascii=False, indent=4)
    with open('train_set_for_classify/x2.json', 'w', encoding="utf-8") as outfile:
        json.dump(x2_train, outfile, ensure_ascii=False, indent=4)

    np.save('train_set_for_classify/y_train.npy', np.asarray(y_train))


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


def save_w2v():
    word_vec_file = KeyedVectors.load_word2vec_format('E:\\CPE#Y4\\NLP\\wiki.th.vec')

    x1 = json.load(open('train_set_for_classify/x1.json', 'r', encoding='utf-8-sig'))
    x2 = json.load(open('train_set_for_classify/x2.json', 'r', encoding='utf-8-sig'))

    x1_train = init_word_vectors(x1, word_vec_file, 40)
    x2_train = init_word_vectors(x2, word_vec_file)
    print(x1_train.shape)
    print(x2_train.shape)

    np.save('train_set_for_classify/x1_train.npy', np.asarray(x1_train))
    np.save('train_set_for_classify/x2_train.npy', np.asarray(x2_train))

# path = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\positive_embedded\\'
# path2 = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
# mask_path = 'E:\CPE#Y4\databaseTF\\npy_for_train\positive_tokenized\\'
# q = np.load(path2 + 'embedded_questions_4000_40_300.npy')
#
# x2_train = []
# x1_train = []
# y_train = []
# for i in range(4000):
#     print(i)
#     tmp = np.load(path + 'positive_question'+str(i)+'.npy')
#     mask = json.load(open(mask_path + 'positive_question' + str(i) + '.json','r',encoding='utf-8-sig'))
#     for j in range(tmp.__len__()):
#         y_train.append(mask[j]["sample_answer_maks"])
#         x1_train.append(q[i])
#         x2_train.append(tmp[j])

# np.save(path + 'x1_train.npy', np.asarray(x1_train))
# np.save(path + 'x2_train.npy', np.asarray(x2_train))

path2 = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
mask_path = 'E:\CPE#Y4\databaseTF\\npy_for_train\positive_tokenized\\'
y_train = []
for i in range(4000):
    print(i)
    mask = json.load(open(mask_path + 'positive_question' + str(i) + '.json','r',encoding='utf-8-sig'))
    for j in range(mask.__len__()):
        # print(np.asarray(mask[j]["sample_answer_maks"]))
        y_train.append(np.asarray(mask[j]["sample_answer_maks"]))

y_train = np.asarray(y_train)
print(y_train[-1])
np.save(path2 + 'y_train.npy', np.asarray(y_train))