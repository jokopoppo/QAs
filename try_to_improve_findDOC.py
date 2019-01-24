import pythainlp
from fill_missing_doc import check_tokenizeJSON , check_cdoc
from pprint import pprint
from usage import rreplace , alarm

def fill_cant_find(path):
    from sqlitedict import SqliteDict
    q, rank, cant = check_rank(path)

    doc = SqliteDict('E:\CPE#Y4\databaseTF\lastest_db\doc_add_missing.sqlite', autocommit=True)
    dict = doc['doc']
    print('Done Initial Dict',)
    for k in cant:
        for word in k:
            if not word or word == '"' or word == '-':
                continue

            found = []
            for i in dict:
                # print(i)
                for j in dict[i]:
                    if word in j:
                        for index in dict[i][j][1:]:
                            found.append(index)
                        print(word, j, end=' ')
            print(word,"LEN", found.__len__())
            if 0 < found.__len__() < 16:
                mean = 0
                min = 10
                for i in found:
                    mean += i[1]
                    if i[1] < min:
                        min = i[1]
                mean = mean / found.__len__()
                found.insert(0, [mean, min])
                try:
                    dict[word[0]][word] = found
                except KeyError:
                    break
                print(found)

    doc['doc'] = dict
    doc.commit()

def check_rank(path):
    file = open(path, mode='r', encoding="utf-8-sig")
    rank = []
    q = []
    cant = []
    for i in file:
        try:
            tmp = int(i.split('rank')[1].split()[0])
        except IndexError:
            tmp = -1
        tmp2 = int(i.split()[1].replace(':', ''))

        if tmp > 25 or tmp < 0 :
            c = i.split("]")[-2].split('[')[-1]
            c = c.split(',')

            for word in range(c.__len__()):
                c[word] = c[word].replace("'", '').strip()

            if not c[0] or c[0] == '"' or c[0] == '-' :
                continue
            cant.append(c)

            q.append(tmp2)
            rank.append(tmp)

    print(q.__len__(), rank.__len__(), cant.__len__())
    for i in range(rank.__len__()):
        print(q[i], rank[i], cant[i])

    return q,rank,cant

q,rank,cant = check_rank("result/result_q_weight5_fill_c[0].txt")
check_tokenizeJSON(1274)

# fill_cant_find("result/result_q_weight5_fill_c[0].txt")
print(cant)



