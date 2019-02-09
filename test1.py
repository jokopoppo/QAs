from pythainlp.number import *
from word2number import w2n

s = ['ควาย','เจ็ด','ยี่สิบ']
thai_number_text = [u'หนึ่ง', u'สอง', u'สาม', u'สี่', u'ห้า', u'หก', u'เจ็ด', u'แปด', u'เก้า']

for i in s:
    print(w2n.word_to_num(i))