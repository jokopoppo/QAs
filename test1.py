import os
import json
import re
import deepcut

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = cleantext.replace('\n', '')
  return ''.join(e for e in cleantext if e not in ['(', ')', '–', '_', ',', '-'])

def get_title(s):
    p = re.compile(' title="(.*)">')
    result = p.search(s)
    return result.group(1)  # group(1) will return the 1st capture.


path = 'E:\CPE#Y4\databaseTF\documents-nsc\\'
saved_path = 'E:\CPE#Y4\databaseTF\\new-documents-tokenize\\'
file = os.listdir(path)

word = set([])

for i in range(file.__len__()):
    print(((i+1)/file.__len__())*100,'. . .',i+1,'/',file.__len__())
    f = open(path + file[i], 'r', encoding="utf-8-sig")
    s = f.read()

    title = get_title(s)
    text = cleanhtml(s)

    title = deepcut.tokenize(title)
    text = deepcut.tokenize(text)
    saved = [list(title),list(text)]
    word = set(word) | set(title) | set(text)
    # print(word)
    with open(saved_path + file[i].replace('.txt','') +'.json', 'w', encoding="utf-8") as outfile:
        json.dump(saved, outfile, ensure_ascii=False)

with open('all_word.json', 'w', encoding="utf-8") as outfile:
    json.dump(list(word), outfile, ensure_ascii=False)



