import json


def hasNumbers(inputString, thai_number_text):
    for i in thai_number_text:
        if inputString.startswith(i) or inputString.endswith(i):
            return True
    return any(char.isdigit() for char in inputString)


def check_question_type(a, question):
    c = a.split()
    n = a.count(' ')

    if n == 0:
        return c[0] in question
    else:
        return c[1] in question and question[question.index(c[1]) - n] == c[0]


def find_question_word(question, question_words):
    for w in question_words:
        c = w.split()
        n = w.count(' ')
        if check_question_type(w, question):
            if n == 0:
                return [question.index(c[0]), c[0]]
            else:
                return [question.index(c[1]), c[1]]


def find_date_candidate(sentence):
    word_candidate_idx = []
    word_candidate = []
    for i in range(sentence[2].__len__()):
        if hasNumbers(sentence[2][i], thai_number_text):
            word_candidate_idx.append(i)
            word_candidate.append(sentence[2][i])
    if word_candidate.__len__() < 1:
        for k in range(sentence[2].__len__()):
            word_candidate_idx.append(i)
            word_candidate.append(sentence[2][i])

    word_candidate.insert(0, sentence[1])
    return word_candidate, word_candidate_idx


def find_candidate(sentence, l):
    word_candidate = []
    word_candidate_idx = []
    for i in range(sentence[2].__len__()):
        if sentence[2][i] in word_class[l]:
            word_candidate.append(sentence[2][i])
            word_candidate_idx.append(i)
    word_candidate.insert(0, sentence[1])

    return word_candidate, word_candidate_idx


def find_answer_word(question, sentence, candidate, question_word_index):
    score = relevance_score(question, sentence[2], candidate, question_word_index)

    idx = score.index(max(score))
    return [max(score), sentence[1], candidate[idx], sentence[2][candidate[idx]]]


def relevance_score(question, sentence, word_candidate_index, question_word_index):
    a = []
    l = 2 * question.__len__()

    for i in word_candidate_index:
        a.append([])
        for j in range(i - l, i + l):
            if (i != j) and (0 <= j < sentence.__len__()) and (sentence[j] in question):
                if question.index(sentence[j]) < question_word_index[0]:
                    a[-1].append([question.index(sentence[j]), j, 1])
                else:
                    a[-1].append([question.index(sentence[j]), j, 1])

    m = question.__len__() - 1

    score = []
    for i in range(a.__len__()):
        tmp = 0
        for j in a[i]:
            tmp += (1 - abs(j[1] - word_candidate_index[i]) / l) * (1 - abs(j[0] - question_word_index[0]) / m)
            # * (1 - doc_rank / doc_n) * (1 - similarity_score/max_similarity_score)
        score.append(tmp)

    return score


thai_number_text = [u'หนึ่ง', u'สอง', u'สาม', u'สี่', u'ห้า', u'หก', u'เจ็ด', u'แปด', u'เก้า', u'สิบ', u'สิบเอ็ด']
question_type = [
    ['กี่', 'ปี ใด', 'ปี อะไร', 'พ.ศ.  อะไร', 'ค.ศ.  อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'พ.ศ. ใด', 'พ.ศ.  ใด',
     'ค.ศ. ใด',
     'ค.ศ.  ใด', 'เท่า ไร', 'เท่า ไหร่', 'เท่า ใด', 'คริสต์ศักราช ใด', 'จำนวน ใด']
    , ['เมื่อ ไร', 'เวลา ใด', 'วัน ใด', 'เมื่อ ใด', 'วัน ที่']  # date format
    , ['ใคร', 'ว่า อะไร', 'ชื่อ อะไร', 'คน ใด', 'คน ไหน', 'คือใคร', 'ผู้ ใด']  # human name
    , ['ประเทศ ใด', 'ประเทศ อะไร'
        , 'จังหวัดใด', 'จังหวัด ใด', 'จังหวัด อะไร'
        , 'เมืองใด', 'เมือง ใด', 'เมือง อะไร'
        , 'ภาค ใด'
        , 'แคว้น ใด'
        , 'ทวีปใด', 'ทวีป อะไร', 'ทวีป ใด', 'ภูมิภาค ไหน'
        , 'ที่ ไหน', 'ที่ ใด', 'ใด', 'ไหน']  # where
    , ['อะไร', 'อย่าง ไร']  # other what, other dai, other nhai
]

question = json.load(open('test_set\\no_space_questions_tokenize.json', mode='r', encoding="utf-8-sig"))
validate_answer = json.load(open('test_set/validate_answer_word.json', mode='r', encoding="utf-8-sig"))
sentence_candidate = json.load(
    open('E:\CPE#Y4\databaseTF\sentence_candidate\\candidate_sen_2_doc_100rank_40len.json', mode='r',
         encoding="utf-8-sig"))

word_class = [[], [], [], [], []]
for i in range(2, word_class.__len__()):
    word_class[i] = set(json.load(open('word_class/' + str(i) + '.json', mode='r', encoding="utf-8-sig")))

answer = []
for i in range(question.__len__()):
    for l in range(question_type.__len__()):
        if any(check_question_type(k, question[i]) for k in question_type[l]):

            question_word_index = find_question_word(question[i], question_type[l])
            rr_score = []
            word_candidate = []
            word_candidate_idx = []
            for j in sentence_candidate[i]:
                if l > 1:
                    word_candidate, word_candidate_idx = find_candidate(j, l)
                elif l == 0:
                    word_candidate, word_candidate_idx = find_date_candidate(j)

                if not word_candidate_idx:
                    continue
                rr_score.append(find_answer_word(question[i], j, word_candidate_idx, question_word_index))
                # print(rr_score[-1])

            rr_score.sort(key=lambda s: s[0], reverse=True)
            answer.append(rr_score[:10])
            print(i,rr_score[:2])
            # print("DONE")
            break

with open('./output/TEST_output.json', 'w', encoding="utf-8") as outfile:
    json.dump(answer, outfile, ensure_ascii=False, indent=4)