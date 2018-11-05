
from pprint import pprint

# index_dir = 'D:/CPE#Y4/databaseTF/index/'
# tokenize_dir = 'D:/CPE#Y4/databaseTF/documents-tokenize/'
#
#
# file = open(index_dir + "14" + ".json")
# data = json.load(file)
#
#
# pprint(data["วอลเลซ เสต็กเนอร์"])
#

# a=[[1,2,3,4,5,7],[5,7],[5,6,7]]
#
# b= list(set.intersection(*map(set,a)))
# print(b)

def save_tokenize():
    import json
    import os
    import deepcut

    datasets_dir = 'D:/CPE#Y4/databaseTF/documents-nsc/'
    save_dir = 'D:/CPE#Y4/databaseTF/documents-tokenize/'

    datasets = os.listdir(datasets_dir)
    fs = []
    for dataset in datasets:
        if(dataset == 'test.txt'):
            break
        fs.append(int((dataset.split("."))[0]))

    fs = sorted(fs)
    fs = fs[0:50000]

    for f in fs :
        dataset_path = os.path.join(datasets_dir, str(f) + ".txt")

        file = open(dataset_path, mode='r', encoding="utf-8-sig")
        file = file.read()

        words = []
        words += deepcut.tokenize(file)
        json.dump(words, open(save_dir + str(f) + '.json', "w"), ensure_ascii=True)

    return

def getKeysJSON():
    import json

    index_dir = 'D:/CPE#Y4/databaseTF/index/'

    file = open(index_dir + "14" + ".json")
    data = json.load(file)

    data = sorted(data)
    n=0
    for k in data:
        n+=1
        k=k.strip()
        if(k and (not k.isspace())):
            print(n,k)


    return

def read_sample_questions():
    import json

    file = open("sample_questions.json", encoding="utf-8-sig")
    data = json.load(file)

    for k in data:
        print(k)

    data = data['data']
    questions = []

    print(data[0])
    for i in data:
        # print(i['question'])
        questions.append(i['question'])
        print(i['answer'])
        questions.append(i['answer'])
    return

from itertools import chain

def find_by_dict():
    import json

    s = ['วอลเลซ เสต็กเนอร์', 'เป็น']
    s.sort()
    fs = []
    for w in s:
        fs.append(w[0])

    fs = list(set(fs))
    print(fs)

    index_dir = 'E:/CPE#Y4/databaseTF/dict/'

    search = []
    for f in fs:

        file = open(index_dir + str(f) + ".json")
        data = json.load(file)

        for i in s:
            print(s)
            if (f == i[0]):
                s.remove(i)
                search.append(data[i])
    return

# import json
#
# index_dir = 'E:\CPE#Y4\databaseTF\documents-tokenize\\'
#
#
# file = open(index_dir + str("818026") + ".json")
# print(file)
# data = json.load(file)
#
# print(data)

a=[[1,2],[1,2],[1,3]]
a = list(set(tuple(element) for element in a))
print(a)


