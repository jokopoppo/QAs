import json
tmp = [{"question_id":1,"question":"สุนัขตัวแรกรับบทเป็นเบนจี้ในภาพยนตร์เรื่อง Benji ที่ออกฉายในปี พ.ศ. 2517 มีชื่อว่าอะไร","answer":"ฮิกกิ้นส์","answer_begin_position ":529,"answer_end_position":538,"article_id":115035}]
data = {}
data['data'] = tmp
print(data)
with open('test,json', 'w' , encoding="utf-8") as outfile:
    json.dump(data,outfile,indent=4,ensure_ascii=False)