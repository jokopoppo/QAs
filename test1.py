from ast import literal_eval
import json

l = [2,3,4,5,6,7,8,9,10]

for label in l:
    print(label)
    n = []
    data = open("train_set_for_classify//" + str(label) + ".txt", "r", encoding="utf-8")
    jon = json.load(open("word_class//" + str(label) + ".json", "r", encoding="utf-8"))
    for i in data:
        i = [j for j in literal_eval(i)]
        # print(i)
        for j in i:
            n.append(j)
    print(n.__len__())
    print(jon.__len__())

    for i in n:
        jon.append(i)

    print(jon.__len__())
    with open("word_class//" + str(label) + ".json", "w", encoding="utf-8") as outfile:
        json.dump(jon, outfile, indent=4, ensure_ascii=False)

