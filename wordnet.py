from pythainlp.corpus import wordnet
from sqlitedict import SqliteDict
import time

start = time.time()
doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc.sqlite', autocommit=True)
dict = doc['doc']
print(time.time() - start)

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'
be_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

al = [alphabet,vowel,e_alphabet,be_alphabet,num]
for a in al :
    for index in a:
        t_word = []
        for word in dict[index]:
            t_word.append(word)

        for word in t_word:
            tmp = dict[index][word]
            synonyms = []
            for syn in wordnet.synsets(word):
                for s in syn.lemma_names('tha'):
                    synonyms.append(s)

            synonyms = list(set(synonyms))
            print(synonyms)

            for i in synonyms:
                try :
                    dict[i[0]][i]
                except KeyError :
                    try :
                        dict[i[0]][i] = tmp
                    except KeyError :
                        continue
start = time.time()
doc['doc'] = dict
doc.commit()
print(time.time() - start)



