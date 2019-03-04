import json

validate = json.load(open("test_set\\new_sample_questions_answer.json", mode='r', encoding="utf-8-sig"))
ans = json.load(open("output_findDoc4000.json", mode='r', encoding="utf-8-sig"))

acc=0
for i in range(validate.__len__()):
    if str(validate[i]) in ans[i]:
        acc+=1

print(acc)