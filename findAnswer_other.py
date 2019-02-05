import json
# import warnings
# warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
# warnings.filterwarnings(action='ignore', category=FutureWarning)
# from gensim.models import Word2Vec
def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def make_sentence_answer(article_id,answer_begin,n=15):
    doc = json.load(
        open('E:\CPE#Y4\databaseTF\documents-tokenize\\' + str(article_id) + '.json', 'r',
             encoding='utf-8-sig'))
    sentence_answer = []
    l = 0
    for j in range(doc.__len__()):
        l += doc[j].__len__()
        if l >= answer_begin - 1:
            for k in range(j - n, j + n):
                try:
                    sentence_answer.append(doc[k])
                except IndexError:
                    break
            break
    return sentence_answer

a = json.load(open('test_set/new_sample_questions.json',encoding='utf-8-sig'))
a = a['data']
question = json.load(open('test_set\\new_sample_questions_tokenize.json', 'r', encoding='utf-8-sig'))

question_index = []
doc_id = []
real_answer = []
question_words = ['กี่', 'อะไร', 'ใด', 'เท่า', 'ปี' ]
wrong = 0
all_rs = []
possible_answer = []

n = 0
# model = Word2Vec.load("E:\CPE#Y4\databaseTF\word2vec_model_lastest\word2vec.model")
ans = []
s_ans = []
wv = []
for i in range(wrong,a.__len__()):
    article_id = a[i]['article_id']
    answer = a[i]['answer']
    answer_begin = a[i]['answer_begin_position ']
    answer_end = a[i]['answer_end_position']
    sentence_answer = make_sentence_answer(article_id, answer_begin)
    for j in question[i]:
        if j == 'ใคร':
            # print(i,answer,question[i])
            # print(sentence_answer)
            n+=1
            ans.append([i,answer])
            s_ans.append(sentence_answer)
            wv.append([])
            for k in sentence_answer:
                if (k in answer) and (k.__len__() >= 2):
                    wv[-1].append(k)

            break
print(n)

string = ''
for i in range(ans.__len__()):
    if wv[i].__len__() < 1 :
        print(wv[i])
        word = []
        for j in s_ans[i]:
            d = similar(ans[i][1], j)
            if d > 0.5 :
                word.append([j, d])
                string += j + '\n'
        word.sort(key=lambda s: s[1], reverse=True)
        print(ans[i], word)


with open("train_set_for_classify/human_name_no_wv.txt", "w", encoding="utf-8") as text_file:
    text_file.write(string)