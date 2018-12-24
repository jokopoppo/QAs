import numpy as np
import matplotlib.pyplot as plt

data = open('result_newDB.txt','r',encoding='utf-8-sig')

a = []
topN = []
for i in data:
    i=i.replace('cant find in best tf-idf', 'ct')
    i=i.replace('cant find in shortest', 'cs')
    i=i.replace('Cant find doc','cd')
    a.append(i.split())
    topN.append(a[-1][3])

for i in range(a.__len__()):

    try:
        topN[i] = int(topN[i].split('rank')[1])
    except IndexError:
        topN[i] = 1000000
print(topN)

rank=[5,10,20,50,100,500,1000,2000,3000,5000,10000]
acc = []
for n in rank:
    acc.append(0)
    for i in topN:
        if i < n :
            acc[-1]+=1
    acc[-1] = acc[-1] / topN.__len__()
    print(n,acc[-1])

t= np.arange(1000)
plt.xlabel('Length of the list')
plt.ylabel('Number of list')
plt.title('Histogram of Shortest list')

plt.plot(rank,acc,'g')
# plt.hist(pool1,50,color='g')
# plt.hist(pool2,50)
plt.grid(axis='y')
plt.show()

