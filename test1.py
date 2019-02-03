a = []
b = []
with open("result_find_answer_word.txt", "r", encoding="utf-8") as text_file:
    for i in text_file:
        a.append(i.split()[0])

with open("result_find_answer_word(1).txt", "r", encoding="utf-8") as text_file:
    for i in text_file:
        b.append(i.split()[0])

print(list(set(b)-set(a)))