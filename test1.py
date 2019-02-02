import editdistance
# import deepcut
def normalized_edit_similarity(a, b):
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

def order_consistency(index_a,index_b,l):
    return 1.0 - abs(index_a - index_b)/l

def extractNumberFromString(string):
    import re
    return re.findall('\d+', string )


def relevance_score(question,sentence,candidate,index):

    a = []
    l = 2*question.__len__()
    for i in c :
        a.append([])
        for j in range(i-l,i+l):
            if j < sentence.__len__() and sentence[j] in question:
                a[-1].append([question.index(sentence[j]),j])

    m = a.__len__()
    score = []
    for i in range(m) :
        tmp = 0
        for j in a[i]:
            tmp += (1-abs(j[1] - candidate[i])/l)*(1-abs(j[0] - index)/m)
        score.append(tmp)

    return max(score)

q = ['ผลไม้', 'ราคา', 'กี่', 'บาท']
s = ['วัน', 'นี้', 'ตอน', 'เที่ยง', 'มา', 'นี', 'ซื้อ', 'ข้าว', 'มัน', 'ไก่', 'จาน', 'ละ', ' ', '35', ' ', 'บาท', ' ', 'กับ', 'ผลไม้', 'ถุง', 'ละ', ' ', '20', ' ', 'บาท', ' ', 'น้าชา', 'อีก', ' ', '10', ' ', 'บาท', ' ', 'รวม', 'แล้ว', 'มา', 'นี', 'ใช้', 'เงิน', 'ไป', ' ', '65', ' ', 'บาท']
c = [13,22,29,41]
relevance_score(q,s,c,2)

