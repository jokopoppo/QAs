from sqlitedict import SqliteDict

dict = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite', autocommit=True)
dict = dict['doc']

n = 0
for k,v in dict.items():
    print(k,v)
    n+=1
    if n > 4 :
        break