import os
import json

def sortIndex_by_string(string):
    e_alphabet = string
    alp = []

    for i in range(e_alphabet.__len__()):
        alp.append({})

    print("alp", alp.__len__())

    dict_dir = 'E:\\CPE#Y4\\databaseTF\\new-dict\\'
    index_dir = 'E:\\CPE#Y4\\databaseTF\\index\\'
    datasets = os.listdir(index_dir)
    fs = []
    for dataset in datasets:
        if (dataset == 'old'):
            continue
        fs.append(int((dataset.split("."))[0]))

    fs = sorted(fs)

    for f in fs:
        print(f)
        c = (json.load(open(index_dir + str(f) + ".json", 'r', encoding='utf-8')))

        delitem = []

        for k in c:

            if not (k and (not k.isspace())):
                delitem.append(k)

            elif k[0] not in e_alphabet:
                delitem.append(k)

        for i in delitem:
            del c[i]

        data = [c]

        for i in data:
            sorted(i)
            for k, v in i.items():
                # print(k)
                try:
                    tmp = e_alphabet.index(k[0])
                    if (alp[tmp].get(k) is None):
                        alp[tmp][k] = []
                    alp[tmp][k] += v
                except ValueError:
                    continue

    for i in range(alp.__len__()):
        finename = dict_dir + str(e_alphabet[i]) + ".json"
        print(finename)
        json.dump(alp[i], open(finename, 'w'), ensure_ascii=True)

    print("Done")

# alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
# vowel = 'เแโใไ'
# e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

e_alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'

sortIndex_by_string(e_alphabet)

