import json
import deepcut
data = json.load(open('test_set/new_sample_questions.json','r',encoding='utf-8-sig'))

q = []
for i in range(data['data'].__len__()):
    q.append([])
    tmp = deepcut.tokenize(data['data'][i]['question'])
    for j in tmp:
        if ' ' not in j or j == ' ':
            q[-1].append(j)
        else:
            tmp2 = j.split()
            for k in tmp2:
                q[-1].append(k)
    print(i,q[-1])

with open('test_set/no_space_questions_tokenize.json', 'w', encoding="utf-8") as outfile:
    json.dump(q, outfile, ensure_ascii=False,indent = 4)