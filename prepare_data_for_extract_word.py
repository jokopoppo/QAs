import os
import json
import numpy as np
from gensim.models import KeyedVectors


def save_y_train():
    path2 = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
    mask_path = 'E:\CPE#Y4\databaseTF\\npy_for_train\\positive_tokenized\\'
    y_train = np.zeros((20000, 40))
    print(y_train.shape)
    for i in range(4000):
        mask = json.load(open(mask_path + 'positive_question' + str(i) + '.json', 'r', encoding='utf-8-sig'))
        for j in range(mask.__len__()):
            if mask[j]["sample_answer_maks"].__len__() < 40:
                for k in range(40 - mask[j]["sample_answer_maks"].__len__()):
                    mask[j]["sample_answer_maks"].insert(0, 0)
            print(i * mask.__len__() + j, np.array(mask[j]["sample_answer_maks"]).__len__())
            y_train[i * mask.__len__() + j] = np.array(mask[j]["sample_answer_maks"])
    # exit()
    print(y_train.shape)
    np.save(path2 + 'y_train.npy', y_train)


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


word_vec_file = KeyedVectors.load_word2vec_format('E:\\CPE#Y4\\NLP\\wiki.th.vec')
path = 'E:\CPE#Y4\databaseTF\\npy_for_train\positive_tokenized\\'
file = os.listdir(path)
question = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
n = 0

x1_for_train = []
x2_for_train = []
for i in file:
    f = json.load(open(path + i, 'r', encoding='utf-8-sig'))
    for j in f:
        x1_for_train.append(question[n])
        x2_for_train.append(j['sample_sentence'])
    n += 1

x1_train = init_word_vectors(x1_for_train, word_vec_file, 40)
x2_train = init_word_vectors(x2_for_train, word_vec_file, 40)

np.save('E:\\CPE#Y4\\databaseTF\\npy_for_train\\x1_train.npy', np.asarray(x1_train))
np.save('E:\\CPE#Y4\\databaseTF\\npy_for_train\\x2_train.npy', np.asarray(x2_train))
