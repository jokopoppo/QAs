import json
from sqlitedict import SqliteDict
import time
from pprint import pprint

start = time.time()
doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite', autocommit=True)
dict = doc['doc']
print(time.time() - start)

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
be_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

al = [alphabet,vowel,e_alphabet,be_alphabet,num]
for a in al :
    for index in a :
        t_word = []
        start = time.time()
        for word in dict[index] :
            t_word.append(word)
        print(time.time() - start)

        for word in t_word:
            if ' ' in word:
                tmp = dict[index][word]
                del dict[index][word]
                word = word.split()
                print(word)
                for i in word:
                    try:
                        check = []
                        tmp2 = dict[i[0]][i]
                        for d, _ in tmp2[1:]:
                            check.append(d)

                        for d, t in tmp[1:]:
                            if d not in check:
                                tmp2.append([d, t])

                        dict[i[0]][i] = tmp2
                    except KeyError:
                        try:
                            dict[i[0]][i] = tmp
                        except KeyError:
                            continue

start = time.time()
doc['doc'] = dict
doc.commit()
print(time.time() - start)