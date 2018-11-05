from pprint import pprint
import json
import deepcut
import time

start = time.time()


s = 'ทางหลวงอินเตอร์สเตตอยู่บนเกาะอะไร'
# s = 'วอลเลซ เสต็กเนอร์เป็นใคร'
# s = 'ในอดีตเมืองคิตะกะมิเป็นส่วนหนึ่งของแคว้นอะไร' # 818026
s = deepcut.tokenize(s)
print(s)
s.sort()
print(s)

fs = []
for w in s:
    fs.append(w[0])

fs.sort()
print(fs)

index_dir = 'E:/CPE#Y4/databaseTF/dict2/'

search = []
for f in range(s.__len__()):
    if s[f][0] != s[f-1][0] :
        file = open(index_dir + str(s[f][0]) + ".json")
        data = json.load(file)

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
        # intersection[i].append([search[i][0],int(j[0])])
        intersection[i].append(int(j[0]))

intersection.sort(key=len)

# for i in range(intersection.__len__()):
#     intersection[i] = list(set(tuple(element) for element in intersection[i]))
#     pprint(intersection[i][0])

answer = set(intersection[0])
for i in range(1,intersection.__len__()):
    if (set(intersection[i]) & answer):

        answer &= set(intersection[i])

answer = list(answer)

n=5
for i in range(answer.__len__()):
    print(answer[i])
    if(i==n):
        break
end = time.time()
print(end - start,'secs')