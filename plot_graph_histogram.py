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

        plt.xlabel('Rank N',size = 25)
        plt.ylabel('Accuracy' , size=25)
        plt.title('Accuracy in N rank',size =25)

        plt.plot(rank, acc,marker='o', label=str(file.index(f)))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.grid(axis='y')
    plt.grid(axis='x')
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.show()

def plot_histogram(file,n,color):

    data = open('result\\' + file, 'r', encoding='utf-8-sig')

    l = []
    for i in data:
        tmp = i.split(']]')[-1].split()
        print(tmp)
        for j in range(tmp.__len__()):
            if tmp[j].isnumeric():
                try:
                    l.append(int(tmp[j+n]))
                    break
                except ValueError:
                    l.append(0)
                    break


    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.hist(l, 50, color=color)
    plt.grid(axis='y',)
    plt.xlabel('Length of list',size=25)
    plt.ylabel('Number of list',size=25)
    plt.title('Histogram of shortest list',size=25)
    plt.show()



file = os.listdir('result/')
file = file[4:]
print(file)

for i in range(file.__len__()):
    print(i,file[i])
# plotAccuracy([file[4]])

plot_histogram(file[4],1,'lightgreen')

