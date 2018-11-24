# coding=utf8

from pprint import pprint
import json
import os
# import deepcut
import time
from heapq import nlargest
from sqlitedict import SqliteDict

def remove_dup(l):
    seen = set()
    newlist = []
    for item in l:
        t = tuple(item)
        if t not in seen:
            newlist.append(item)
            seen.add(t)
    return newlist
# TODO fix this for new algorithm

# s = 'นักบุญทาอีสในคริสต์ศตวรรษที่ 4เป็นชาวอะไร'
# s = 'ทางหลวงอินเตอร์สเตตอยู่บนเกาะอะไร'
# s = 'วอลเลซ เสต็กเนอร์เป็นใคร'
# s = 'ในอดีตเมืองคิตะกะมิเป็นส่วนหนึ่งของแคว้นอะไร' # 818026
# s = '"หนึ่งต่อเจ็ด" ออกฉายในปีใด' ##
# s = 'สมัยก่อนคิตะกะมิเป็นเมืองที่อยู่ในแคว้นใด' #
s = 'อุตะมะโระอาศัยอยู่ที่บ้านของใคร'

dict = SqliteDict('db.sqlite', autocommit=True)
begin = time.time()
alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

index_dir = 'E:/CPE#Y4/databaseTF/dict2/'
file = open("questions_tokenize.json", mode = 'r' , encoding="utf-8-sig")
data = json.load(file)
validate = json.load(open("questions_answer.json", mode = 'r' , encoding="utf-8-sig"))
# validate = [1]
# data = [deepcut.tokenize(s)]
doc = 60
data = data[doc:]
print(data.__len__())
save = 0
string = ''
acc=0
for s in data:
    string += "question " + str(doc)
    print("question",doc,s,validate[doc])

    start = time.time()

    # print(s)
    s.sort()
    # print(s)

    search = []
    cantfind = []
    notindex = []

    now = None
    for f in range(s.__len__()):
        if(s[f].isspace()):
            continue

        if s[f-1][0] != s[f][0]:
            now = dict.get(s[f][0])

        tmp = None
        if(now != None):
            tmp = now.get(s[f])
        if tmp != None :
            search.append((s[f], tmp))
        else:
            cantfind.append((s[f]))
    rank = []
    for i in range(search.__len__()):
        # print(search[i][0], search[i][1][0][0])
        rank.append(search[i][1][0][0])
    # rank = sorted(rank, key=lambda l: l[1], reverse=True)

    intersection = []
    for i in search:
        intersection.append([])
        for j in range(1,i[1].__len__()):
            try:
                intersection[-1].append([i[1][j][0],i[1][j][4]])
            except IndexError:
                continue
        intersection[-1] = remove_dup(intersection[-1])

    intersection = [x for _, x in sorted(zip(rank, intersection),reverse=True)]

    intersection=[intersection[0]]
    answer_index = []
    count = []

    # for i in intersection[rank[0][0]]:
    #     answer_index.append(i[0])
    #     count.append(0)
    # print(answer_index)

    for i in intersection:
        for j in i:

            if j[0] in answer_index:
                count[answer_index.index(j[0])] += j[1]
            else:
                answer_index.append(j[0])
                count.append(j[1])

    answer_n = nlargest(100, count)
    answer = []
    for i in answer_n:
        index = count.index(i)
        answer.append(answer_index[index])
        answer_index.pop(index)
        count.pop(index)
    print(answer_n)
    print(answer)
    answer = list(answer)

    ans_int = ''
    shorttest = []
    for i in intersection[0]:
        shorttest.append(i[0])

    try:
        ans_int = ' ' + str(shorttest.index(str(validate[doc]))) + ' '
    except ValueError:
        ans_int = ' cant find in shortest '

    try:
        if answer.index(str(validate[doc])) < 6 :
            string += ': 1'
        else:
            string += ': 0'
        string += " rank" + str(answer.index(str(validate[doc]))) + ' ||' + ans_int + str(cantfind) + str(notindex) + '\n'
    except ValueError:
        string += ": 0 Cant find doc" + ' ||' + ans_int + str(cantfind) + str(notindex) + '\n'

    end = time.time()
    print(end - start, 'secs')
    doc+=1
    save+=1
    if save==4 or doc==100:
        with open("result_tf-idf.txt", "a" , encoding = "utf-8") as text_file:
            text_file.write(string)
        save = 0
        string = ''
    if doc ==100:
        break

end = time.time()
print(end - begin, 'secs')
os.system("shutdown /s /t 90")


