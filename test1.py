import pythainlp
from fill_missing_doc import check_tokenizeJSON



q = [3043 , 3147 , 3583]
#
# for i in q :
#     check_tokenizeJSON(i)
s = ['โมเมนตัมคือ' , 'เคลย์มอร์คือ' , 'คือไมโอซินคือ' ,'คือ']
r = []
for i in s:
    if ' ' in i:
        for j in i.split():
            s.append(j)
    elif i.endswith('คือ'):
        r.append(i)
        s.append(i.rreplace('คือ', ' '))
for i in r:
    s.remove(i)
print(s)