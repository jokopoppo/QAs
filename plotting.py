import matplotlib.pyplot as plt
import os
from pprint import pprint
def plotAccuracy(file):
    for f in file :
        data = open('result\\'+f, 'r', encoding='utf-8-sig')

        a = []
        topN = []
        for i in data:
            i = i.replace('cant find in best tf-idf', 'ct')
            i = i.replace('cant find in shortest', 'cs')
            i = i.replace('Cant find doc', 'cd')
            a.append(i.split())

            try:
                topN.append(a[-1][3])
            except IndexError:
                print(a[-1])
                exit(0)
        if(topN.__len__() < 4000):
            continue
        for i in range(a.__len__()):
            try:
                topN[i] = int(topN[i].split('rank')[1])
            except IndexError:
                topN[i] = 1000000
        # print(topN)

        rank = [1,5, 10, 20,30, 50, 100 ,200 ,300]
        acc = []
        for n in rank:
            acc.append(0)
            for i in topN:
                if i < n:
                    acc[-1] += 1
            acc[-1] = acc[-1] / topN.__len__()
            # print(n, acc[-1])

        plt.xlabel('Accuracy')
        plt.ylabel('Rank N ')
        plt.title('Accuracy in N rank')

        plt.plot(rank, acc,marker='o', label=str(file.index(f)))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.grid(axis='y')
    plt.grid(axis='x')

    plt.show()

file = os.listdir('result/')
print(file)
file.remove('old_result')
file.remove('addSyms')
file.remove('n_q')
for i in range(file.__len__()):
    print(i,file[i])
plotAccuracy(file)

# f = file[8]
# print(f)
# data = open('result\\'+f, 'r', encoding='utf-8-sig')

# l1 = []
# l0 = []
# for i in data:
#     i=i.split(']')
#     i[-2] = i[-2].split()
#     l1.append(int(i[-2][0]))
#     l0.append(int(i[-2][1]))
# plt.hist(l0,100,color='g')
# plt.show()

# f=file[3]
# print(f)
# data = open('result\\'+f, 'r', encoding='utf-8-sig')
#
# no=[]
# for i in data:
#     if 'Cant find doc' in i :
#         i=i.split(' || ')
#         i[0] = i[0].split()
#         i[1] = i[1].split('[[')
#         i[1][1] = i[1][1].split(", '']]")
#         i[1][1][0] = i[1][1][0].split("'")
#         no.append([i[0][1].split(':')[0],i[1][1][0][1]])
# print(no.__len__())
# pprint(no)