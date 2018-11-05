from typing import List, Any

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=FutureWarning)

from gensim.models import Word2Vec

import deepcut
import os
import json, codecs
import re
import json
import shutil

COUNT = 1000

# pipfirebase = firebase.FirebaseApplication('https://nsc2017-379b3.firebaseio.com/', None)

def lineIndex(dataset_path):

    file = open(dataset_path, mode = 'r' , encoding="utf-8-sig")
    word_count = 0
    char_count = 0

    print(dataset_path)
    print("------------------------------------------------")
    # print(str(f))
    file = file.read()

    words = []
    words += deepcut.tokenize(file)

    json.dump(words, open(tokenize_dir + str(f) + '.json', "w"), ensure_ascii=True)
    for word in words :

        word = word.replace("\ufeff", "")

        tmp = result.get(word)

        if tmp is None:
            result[word] = []
        result[word].append((str(f), word_count, char_count, len(word)))

        char_count = char_count + len(word)
        word_count = word_count + 1


    try:
        # os.remove(dataset_path)
        print("file %s has move" % dataset_path)
        return words
    except:  ## Show an error ##
        print("Error: %s file not found" % dataset_path)

datasets_dir = 'D:/CPE#Y4/databaseTF/documents-nsc/'
index_dir = 'D:/CPE#Y4/databaseTF/index/'
tokenize_dir = 'D:/CPE#Y4/databaseTF/documents-tokenize/'
datasets = os.listdir(datasets_dir)
# print(datasets.__len__())
fs = []
for dataset in datasets:
    if(dataset == 'test.txt'):
        break
    fs.append(int((dataset.split("."))[0]))

fs = sorted(fs)
fs = fs[112000:]
file_count_index = 45
file_count = 0

result = {}
tokendata=[]
model = Word2Vec.load("w2v_all_corpus.bin")
for f in fs:
    dataset_path = os.path.join(datasets_dir, str(f) + ".txt")
    tokendata=lineIndex(dataset_path)

    words = list(model.wv.vocab)
    print("Words    :", words.__len__())

    model.build_vocab(tokendata, update=True)
    model.train(tokendata, total_examples=1, epochs=1)

    words = list(model.wv.vocab)
    print("Words    :", words.__len__())

    file_count = file_count + 1
    print(file_count)
    # print(result)
    if file_count_index == 1000:
        break
    if file_count == 2000:
        model.save('w2v_all_corpus.bin')
        model = Word2Vec.load("w2v_all_corpus.bin")

        finename = index_dir + str(file_count_index) + ".json"
        sorted(result)

        json.dump(result, open(finename, "w"), ensure_ascii=True)
        # with open(finename, 'wb') as f:
        #     json.dump(result, codecs.getwriter('utf-8')(f), ensure_ascii=False)
        file_count_index += 1
        file_count = 0
        result = {}


os.system("shutdown /s /t 90")