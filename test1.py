import editdistance
from pythainlp.corpus import stopwords
# import deepcut
def normalized_edit_similarity(a, b):
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

def order_consistency(index_a,index_b,l):
    return 1.0 - abs(index_a - index_b)/l

def extractNumberFromString(string):
    import re
    return re.findall('\d+', string )


def relevance_score(question,sentence,candidate,question_word):

    for i in question:
        if i == ' ':
            question.remove(i)
        for w in question_words:
            if (w != question_word) and (i.endswith(w) and i.startswith(w)):
                print(i)
                question.remove(i)
                break
    # print(question)
    # print(sentence)
    a = []
    question_word_index = question.index(question_word)
    l = 2*question.__len__()
    for i in candidate :
        a.append([])
        for j in range(i-l,i+l):
            if (i != j) and (0 <= j < sentence.__len__()) and (sentence[j] in question):
                if question.index(sentence[j]) < question_word_index:
                    a[-1].append([question.index(sentence[j]), j, 0.5])
                else:
                    a[-1].append([question.index(sentence[j]), j, 0.25])
        print(a[-1])

    m = question.__len__() - 1

    score = []
    for i in range(a.__len__()) :
        tmp = 0
        for j in a[i]:
            tmp += (1-abs(j[1] - candidate[i])/l)*(1 - abs(j[0] - question_word_index)/m + j[2])
        score.append(tmp)

    return score

question_words = stopwords.words('thai')
question_words.append('กี่')
question_words.append('ใด')

q = ['ผลไม้', 'ราคา', 'กี่', 'บาท']
s = ['วัน', 'นี้', 'ตอน', 'เที่ยง', 'มา', 'นี', 'ซื้อ', 'ข้าว', 'มัน', 'ไก่', 'จาน', 'ละ', ' ', '35', ' ', 'บาท', ' ', 'กับ', 'ผลไม้', 'ถุง', 'ละ', ' ', '20', ' ', 'บาท', ' ', 'น้าชา', 'อีก', ' ', '10', ' ', 'บาท', ' ', 'รวม', 'แล้ว', 'มา', 'นี', 'ใช้', 'เงิน', 'ไป', ' ', '65', ' ', 'บาท']
c = [13, 22, 29, 41]

# q = ['ปาเวล เนดเวต', 'ได้', 'รับ', 'การ', 'แต่งตั้ง', 'เป็น', 'กัปตัน', 'ทีม', 'ใน', 'การ', 'แข่งขัน', 'ฟุตบอล', 'ชิง', 'แชมป์', 'แห่ง', 'ชาติ', 'ยุโรป', 'ใน', 'ปี', 'ใด']
# s = ['รับ', 'การ', 'แต่งตั้ง', 'เป็น', 'กัปตัน', 'ทีม', 'ใน', 'การ', 'แข่งขัน', 'ฟุตบอล', 'ชิง', 'แชมป์', 'แห่ง', 'ชาติ', 'ยุโรป', ' ', '2004', ' ', 'ที่', 'เช็ก', 'เกียตกรอบ', 'รอง', 'ชนะ', 'เลิศ', 'ด้วย', 'การ', 'แพ้', 'กรีซ', ' ', 'แต่']
# c = [16]
score = relevance_score(q,s,c,'กี่')
print(score)
print(score.index(max(score)))
print(s[c[score.index(max(score))]])