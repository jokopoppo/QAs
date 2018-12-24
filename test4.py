import json
from pprint import pprint
from sqlitedict import SqliteDict
import itertools
import time
doc = SqliteDict('doc.sqlite' , autocommit=True)
dict = SqliteDict('db.sqlite' , autocommit=True)
dir = 'E:\CPE#Y4\databaseTF\dict2\\'

# all = {}
# for i in dict:
#     print(i)
#     tmp = dict[i] # dict a
#     for j in tmp: # j = ant
#         # print(j)
#         ant = []
#         for k in tmp[j] :
#             try:
#                 ant.append([k[0],k[4]])
#             except IndexError:
#                 ant.append([k[0],-1])
#
#         mean = 0
#         for v in ant:
#             mean += v[1]
#         mean = mean / ant.__len__()
#         tfidf = [mean, min(ant, key=lambda x: x[1])[1]]
#         ant.insert(0,tfidf)
#
#         ant = list(ant for ant, _ in itertools.groupby(ant))
#         tmp[j] = ant
#     all[i] = tmp
#     # break
#
# for k in all:
#     print(k)
# doc['doc'] = all
# doc.commit()

a = [['a',[[8,2],[2,3],[4,5]]],
     ['b',[[1,2],[3,4]]],
     ['c',[[5,2],[3,4]]]
     ]

a.sort(key = lambda s: s[1][0][0],reverse=True)

b=' a '
if b[0] == ' ' or b[-1] == ' ':
     b = b.strip()
print(b)