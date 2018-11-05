
from pprint import pprint
import os
import json
import re
alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
alp = []
vow = []
oth = {}
for i in range(e_alphabet.__len__()):
    alp.append({})
for i in range(vowel.__len__()):
    vow.append({})

print("alp", alp.__len__(), "vow", vow.__len__())

dict_dir = 'E:/CPE#Y4/databaseTF/dict2/'
index_dir = 'E:/CPE#Y4/databaseTF/index/'
datasets = os.listdir(index_dir)
fs = []
for dataset in datasets:
    if(dataset == 'test.txt'):
        break
    fs.append(int((dataset.split("."))[0]))

fs = sorted(fs)

for f in fs :
    print(f)
    c = (json.load(open(index_dir + str(f) + ".json")))

    delitem = []

    for k in c:

        if not(k and (not k.isspace())):
            delitem.append(k)

        elif ((k[0] in alphabet) or (k[0] in e_alphabet) or (k[0] in vowel)):
            delitem.append(k)

    for i in delitem:
        del c[i]

    data = [c]

    for i in data :
        sorted(i)
        for k, v in i.items():
            # print(k)

            try:
                tmp = e_alphabet.index(k[0])
                if (alp[tmp].get(k) is None) :
                    alp[tmp][k] = []
                alp[tmp][k]+=v
            except ValueError:
                try:
                    tmp = vowel.index(k[0])
                    if(vow[tmp].get(k) is None):
                        vow[tmp][k] = []
                    vow[tmp][k]+=v
                except ValueError:
                    if(oth.get(k) is None):
                        oth[k] = []
                    oth[k]+=v


# for i in range(alp.__len__()):
#     finename = dict_dir + str(e_alphabet[i]) + ".json"
#     json.dump(alp[i],open(finename,'w'), ensure_ascii=True)

# for i in range(vow.__len__()):
#     finename = dict_dir + str(vowel[i]) + ".json"
#     json.dump(vow[i],open(finename,'w'), ensure_ascii=True)

finename = dict_dir + str("oth") + ".json"
json.dump(oth, open(finename,'w'), ensure_ascii=True)

