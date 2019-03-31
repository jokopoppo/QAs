import os
import json

def lineIndex(dataset_path,f):


    word_count = 0
    char_count = 0

    words = json.load(open(dataset_path, "r",encoding='utf-8'))

    for i in words:
        for word in i :

            word = word.replace("\ufeff", "")

            tmp = result.get(word)

            if tmp is None:
                result[word] = []
            # result[word].append((str(f), word_count, char_count, len(word)))
            result[word].append((str(f), word_count, char_count, len(word)))
            char_count = char_count + len(word)
            word_count = word_count + 1

    try:
        print("file %s has move" % dataset_path)
    except:
        print("Error: %s file not found" % dataset_path)

index_dir = 'E:/CPE#Y4/databaseTF/index/'
tokenize_dir = 'E:/CPE#Y4/databaseTF/new-documents-tokenize/'
fs = os.listdir(tokenize_dir)

file_count_index = 12
file_count = 0

result = {}
for f in fs[120000:]:
    dataset_path = os.path.join(tokenize_dir, str(f))
    lineIndex(dataset_path,str(f).replace(".json",""))
    file_count = file_count + 1
    print(file_count)
    # print(result)
    if file_count_index == 1000:
        break
    if file_count == 10000:
        finename = index_dir + str(file_count_index) + ".json"
        sorted(result)
        json.dump(result, open(finename, "w",encoding='utf-8'), ensure_ascii=False)
        file_count_index += 1
        file_count = 0
        result = {}

finename = index_dir + str(file_count_index) + ".json"
sorted(result)
json.dump(result, open(finename, "w",encoding='utf-8'), ensure_ascii=False)
# os.system("shutdown /s /t 90")