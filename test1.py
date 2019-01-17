import pythainlp
from fill_missing_doc import check_tokenizeJSON

from usage import rreplace

q = [3043 , 3147 , 3583]
#
# for i in q :
#     check_tokenizeJSON(i)
s = ['โมเมนตัมคือ' , 'เคลย์มอร์คือ' , 'คือไมโอซินคือ' ,'คือ']
r = []
n=0

for i in s:
    if ' ' in i:
        r.append(i)
        for j in i.split():
            s.append(j)
    elif i.endswith('คือ'):
        r.append(i)
        s.append(rreplace(i,'คือ',' ',1))
for i in r:
    s.remove(i)
print(s)