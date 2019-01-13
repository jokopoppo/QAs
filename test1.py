# from pythainlp.corpus import wordnet
import pythainlp
import json
# import deepcut
from sqlitedict import SqliteDict
from pprint import pprint
from pythainlp.corpus import stopwords
import time
from pythainlp.tokenize import word_tokenize
# dict = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc.sqlite', autocommit=True)
# dict = dict['doc']

# q = 10
# file = open("test_set\\new_sample_questions_tokenize.json", mode='r', encoding="utf-8-sig")
# data = json.load(file)
# validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
# # print(data[q] , validate[q])
#
# doc = 'E:\CPE#Y4\databaseTF\documents-tokenize\\'
# db = json.load(open(doc + '348427' + '.json'))
# # print(db)
#
# result = open('result\\result_rQuestionWordsAndCut_shortest1st2nd.txt', mode='r', encoding="utf-8-sig")
# cdoc = 0
# for i in result:
#     if 'cdoc' in i :
#         cdoc+=1
#         print(i)
#
# print(cdoc)
words = stopwords.words('thai')

n_q = json.load(open("no_stop_words_questions_.json", mode='r', encoding="utf-8-sig"))

s = 'จังหวัดไหน'
# print(deepcut.tokenize(s))
# print(pythainlp.word_tokenize(s,engine = 'deepcut'))


