from fill_missing_doc import check_tokenizeJSON

path = 'result/result_q_weight5_fill_c[0].txt'
file = open(path, mode='r', encoding="utf-8-sig")

q = []

for i in file:
    tmp = i.split()[3].split('rank')[-1]
    num = i.split()[1].split(':')[0]
    tmp2 = i.split(']]')[-1].split()
    for j in tmp2 :
        if j.isnumeric():
            print(tmp,j)
            q.append([int(num),int(tmp),int(j)])
            break

q.sort(key=lambda s: s[1] ,reverse=True)
print(q)

for i in q[:7]:
    check_tokenizeJSON(i[0])
