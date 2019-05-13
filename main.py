from findDocuments_improve import *
from findSentence import *
from findAnswer_improve import *
import json

if (__name__ == '__main__'):

    ## find documents

    es = Elasticsearch()

    # es_index(es, 111266)

    q = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))

    candidate_doc = []

    for i in range(q.__len__()):
        candidate_doc.append(search_index(q[i]))
        print(i, candidate_doc[-1])

    with open('document_candidate\\candidate_doc_ESsearch_w_text_boost3_q_no_space.json', 'w',
              encoding="utf-8") as outfile:
        json.dump(candidate_doc, outfile, ensure_ascii=False)

    ## find sentences

    validate_doc = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
    validate_sentences = json.load(open("test_set\\validate_sentences_40.json", mode='r', encoding="utf-8-sig"))
    candidate_doc = json.load(
        open("document_candidate/candidate_doc_ESsearch_w_text_boost3_q_no_space.json", mode='r', encoding="utf-8-sig"))

    validate_answer = []
    data = json.load(open('test_set/new_sample_questions.json', mode='r', encoding="utf-8-sig"))
    for i in data['data']:
        validate_answer.append(i['answer'])

    es = Elasticsearch()
    path = 'E:\\CPE#Y4\\databaseTF\\new-documents-tokenize\\'
    acc = 0

    sentence_candidate = []
    n_doc = 2
    for i in range(validate_doc.__len__()):
        sentence_rank = []
        for j in candidate_doc[i][:n_doc]:
            doc = query_doc_data(j)
            sentences = sentences_in_doc(doc, 20, 40)
            for k in sentences:
                scores = sentence_similar(k, q[i])
                sentence_rank.append([scores, j, k])

        sentence_rank.sort(key=lambda s: s[0], reverse=True)
        sentence_rank = unique_items(sentence_rank)

        sentence_rank = sentence_rank[:100]
        sentence_candidate.append(sentence_rank)
        acc += sentence_acc()

    print(acc)
    with open('E:\\CPE#Y4\\databaseTF\\sentence_candidate\\candidate_sen_2_doc_100rank_40len.json',
              'w', encoding="utf-8") as outfile:
        json.dump(sentence_candidate, outfile, ensure_ascii=False)

    ## find answer

    answer = findAnswer()
    with open('./output/output_answer_4000_2doc_10rank.json', 'w', encoding="utf-8") as outfile:
        json.dump(answer, outfile, ensure_ascii=False, indent=4)
