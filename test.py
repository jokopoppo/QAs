import numpy as np
import json


def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()


def MRR_score_with_list(l, n):
    l = np.array(l)
    l += 1
    score = 0
    for i in l:
        if i > 0:
            score += 1 / i
    return score / n


path2 = 'E:\\CPE#Y4\\databaseTF\\npy_for_train\\'
# sen = json.load(open('E:\\CPE#Y4\\databaseTF\\sentence_candidate\\candidate_sen_2_doc_100rank_40len.json', 'r',
#                      encoding='utf-8-sig'))
y_pred = np.load('y_pred_Bidirectional.npy')
q_index = np.load('q_index.npy')
sen = np.load('sen.npy')
# y_pred = y_pred.reshape((39629, 10, 40))
y_pred = y_pred.argmax(axis=2)
print(y_pred.shape)

ans = []
check = []
for i in range(4000):
    check.append(-1)
    ans.append([])
for i in range(y_pred.__len__()):
    for j in range(y_pred[i].__len__()):
        if y_pred[i][j] == 1:
            try:
                if sen[i][j] != " ":
                    # print(sen[i][j])
                    ans[q_index[i]].append(sen[i][j])
            except:
                pass

answer = json.load(open('test_set/validate_answer_word.json', 'r', encoding='utf-8-sig'))

for i in range(ans.__len__()):
    for j in range(ans[i].__len__()):
        score = similar(answer[i], ans[i][j])
        if score >= 0.5:
            check[i] = j
            break

print(check)
print(MRR_score_with_list(check, 3106))
