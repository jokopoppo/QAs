import json
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = cleantext.replace('\n', '')
  return ''.join(e for e in cleantext if e not in ['(', ')', '–', '_', ',', '-'])

def find_new_position(v, pos, answer):
    doc_path = 'E:\CPE#Y4\databaseTF\documents-nsc\\' + str(validate_doc[v]) + '.txt'
    raw = open(doc_path, 'r', encoding='utf-8-sig')

    for i in raw:
        raw_doc = list(i)
        raw_doc[pos[0] - 1: pos[1]] = 'NEWaNSWER'

        raw_doc = cleanhtml(''.join(raw_doc))

    # print(raw_doc)
    new_idx = raw_doc.index('NEWaNSWER')

    path = 'E:\CPE#Y4\databaseTF\\new-documents-tokenize\\' + str(validate_doc[v]) + '.json'
    doc = json.load(open(path, mode='r', encoding="utf-8-sig"))
    new_doc = ''.join(doc[1])
    if answer == new_doc[new_idx:new_idx + pos[2]]:
        # print(answer, new_doc[new_idx:new_idx + pos[2]])
        return new_idx, new_idx + pos[2]
    else:
        # print('ERROR answer not match new positions')
        print(new_doc)
        print(v,answer, new_doc[new_idx:new_idx + pos[2]])
        return new_idx, new_idx + pos[2]

validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
data = json.load(open('test_set/new_sample_questions.json', 'r', encoding='utf-8-sig'))
pos = []
answer = []
for i in data['data']:
    pos.append([i['answer_begin_position '], i['answer_end_position'],
                i['answer_end_position'] - i['answer_begin_position ']])
    answer.append(i['answer'])
    # print(pos[-1])

new_pos = []
for v in range(validate_doc.__len__()):
    new_pos.append(find_new_position(v,pos[v],answer[v]))

with open('test_set\\new_answer_positions.json', 'w', encoding="utf-8") as outfile:
    json.dump(new_pos, outfile, ensure_ascii=False)
