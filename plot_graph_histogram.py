import matplotlib.pyplot as plt
import os
from pprint import pprint
import json
import random

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

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

def plotAccuracy_withList(topN,label):

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

    plt.plot(rank, acc,marker='o', label=label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.grid(axis='y')
    plt.grid(axis='x')
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)

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

def plot_histogram_with_list(data,color,label):
    # This is  the colormap I'd like to use.
    # cm = plt.cm.get_cmap('RdYlBu_r')

    # Plot histogram.
    # n, bins, patches = plt.hist(data, 50,color=color,alpha=0.5,label=[i for i in range(data.__len__())])
    # bin_centers = 0.5 * (bins[:-1] + bins[1:])

    # scale values to interval [0,1]
    # col = bin_centers - min(bin_centers)
    # col /= max(col)

    # for c, p in zip(col, patches):
    #     plt.setp(p, 'facecolor', cm(c))

    plt.hist(data, 4000, color=color, alpha=0.5, label=[i for i in label])

    plt.legend(loc='upper right')
    plt.tick_params(axis='x', labelsize=10)
    plt.tick_params(axis='y', labelsize=10)
    plt.grid(axis='y',)
    plt.xlabel('Similarity Score',size=15)
    plt.ylabel('Number of Answer',size=15)
    plt.title('Histogram of Similarity',size=15)

    plt.show()


color = []
r = lambda: random.randint(0, 255)
color.append('#%02X%02X%02X' % (r(), r(), r()))

test_output = json.load(open('test_output.json', 'r', encoding='utf-8'))
no_word = json.load(open('no_word.json', 'r', encoding='utf-8'))
validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))

acc = []
out_of_range = 0
for i in range(no_word.__len__()):
    try:
        print(i,test_output[i].index(str(validate[i])))
        acc.append(test_output[i].index(str(validate[i])))
        if test_output[i].index(str(validate[i])) > 5:
            out_of_range+=1
    except ValueError:
        print(i, no_word[i])

print(acc,out_of_range)
# plot_histogram_with_list(acc,color,'accuracy in n rank')
plotAccuracy(['result_q_weight5_fill_c[0](best).txt'])
plotAccuracy_withList(acc,'new-preprocess')
plt.show()