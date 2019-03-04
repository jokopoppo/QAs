import json

def sort_and_save_candidate(f,n_doc,n_rank):
    tmp = []

    for file in f:
        inp = json.load(open("E:\\CPE#Y4\\databaseTF\\candidate_sentence\\" + file, "r", encoding="utf-8"))

        for i in range(inp.__len__()):
            print(str(i + 1) + "/" + str(inp.__len__()))
            print(inp[i].__len__())
            tmp.append([])
            for j in inp[i][:n_doc]:
                for k in j[:n_rank]:
                    k['doc_rank'] = inp[i].index(j)
                    tmp[-1].append(k)
            # print(tmp[-1].__len__())
        print()

        for i in range(tmp.__len__()):
            print(str(i + 1) + "/" + str(tmp.__len__()))
            tmp[i] = sorted(tmp[i], key=lambda k: k['similarity_score'])
            tmp[i] = tmp[i]

    print("DUMP !!!")
    with open('candidate_sentences4000_top' + str(n_doc) + 'doc_rank' + str(n_rank) + '.json', 'w', encoding="utf-8") as outfile:
        json.dump(tmp, outfile, ensure_ascii=False)

def append_candidate(f):
    inp = json.load(open(f[0], "r", encoding="utf-8"))
    tmp = json.load(open(f[1], "r", encoding="utf-8"))

    for i in tmp:
        print(i.__len__())
        inp.append(i)

    with open('candidate_sentences4000[1].json', 'w', encoding="utf-8") as outfile:
        json.dump(inp, outfile,ensure_ascii=False,indent=1)

f = ['candidate_sentences_492.json','candidate_sentences[2000-4000].json']
sort_and_save_candidate(f,3,1000)
# append_candidate(f)


