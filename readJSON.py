from pprint import pprint
import json
import deepcut
import time
# TODO fix this for better intersection


# s = 'ทางหลวงอินเตอร์สเตตอยู่บนเกาะอะไร'
# s = 'วอลเลซ เสต็กเนอร์เป็นใคร'
# s = 'ในอดีตเมืองคิตะกะมิเป็นส่วนหนึ่งของแคว้นอะไร' # 818026
# s = '"หนึ่งต่อเจ็ด" ออกฉายในปีใด' ##
# s = deepcut.tokenize(s)

alphabet = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
vowel = 'เแโใไ'
e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

index_dir = 'E:/CPE#Y4/databaseTF/dict2/'
file = open("questions_tokenize.json", mode = 'r' , encoding="utf-8-sig")
data = json.load(file)

classify = []
start = time.time()
for s in data:

    print(s)
    s.sort()
    print(s)

    fs = []
    for w in s:
        fs.append(w[0])

    fs.sort()
    print(fs)

    search = []
    data = None
    for f in range(s.__len__()):
        if (s[f][0] != s[f-1][0]) and ((s[f][0] in alphabet) or (s[f][0] in e_alphabet) or (s[f][0] in vowel)) :

            file = open(index_dir + str(s[f][0]) + ".json")
            data = json.load(file)
        elif data == None:
            continue

        tmp = data.get(s[f])
        if  tmp != None :
            search.append((s[f], tmp))


    rank = []
    for i in search:
        rank.append([i[0],i[1][0][4]])

    rank = sorted(rank,key=lambda l:l[1], reverse=True)
    print(rank)
    intersection = []

    for i in range(search.__len__()) :
        intersection.append([])
        for j in search[i][1]:
            intersection[i].append([search[i][0],int(j[0])])
            # intersection[i].append(int(j[0]))

    intersection.sort(key=len)
    print(intersection[0].__len__(),intersection[0][0][0])
    classify.append((intersection[0].__len__(),intersection[0][0][0]))
    # answer = set(intersection[0])
    # for i in range(1,intersection.__len__()):
    #     if (set(intersection[i]) & answer):
    #         answer &= set(intersection[i])
    #
    # answer = list(answer)
    #
    # n=10
    # for i in range(answer.__len__()):
    #     if (i == n):
    #         break
    #     print(answer[i])

pprint(classify)

end = time.time()
print(end - start,'secs')