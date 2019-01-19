from usage import rreplace
s = ['ยกตรี คือ', 'เฮเลน โกลก', 'จักรพรรดิไทโช คือ', 'ใคร']
from pythainlp.corpus import stopwords

suffix = ['คือ', 'กี่', 'ใด']
r = []
for i in s:
    print(i)
    if ' ' in i:
        for j in i.split():
            s.append(j)

        r.append(i)
        print(s)
        continue
    for j in suffix:
        if i.endswith(j):
            s.append(rreplace(i, j, ' ', 1))
            r.append(i)
            break
for i in r :
    s.remove(i)
print(s)