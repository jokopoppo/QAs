# coding=utf8

def save_tokenize():
    import json
    import os
    import deepcut

    datasets_dir = 'D:/CPE#Y4/databaseTF/documents-nsc/'
    save_dir = 'D:/CPE#Y4/databaseTF/documents-tokenize/'

    datasets = os.listdir(datasets_dir)
    fs = []
    for dataset in datasets:
        if(dataset == 'test.txt'):
            break
        fs.append(int((dataset.split("."))[0]))

    fs = sorted(fs)
    fs = fs[0:50000]

    for f in fs :
        dataset_path = os.path.join(datasets_dir, str(f) + ".txt")

        file = open(dataset_path, mode='r', encoding="utf-8-sig")
        file = file.read()

        words = []
        words += deepcut.tokenize(file)
        json.dump(words, open(save_dir + str(f) + '.json', "w"), ensure_ascii=True)

    return

def getKeysJSON():
    import json

    index_dir = 'D:/CPE#Y4/databaseTF/index/'

    file = open(index_dir + "14" + ".json")
    data = json.load(file)

    data = sorted(data)
    n=0
    for k in data:
        n+=1
        k=k.strip()
        if(k and (not k.isspace())):
            print(n,k)


    return

def read_sample_questions():
    import json

    file = open("questions.json", encoding="utf-8-sig")
    data = json.load(file)

    for k in data:
        print(k)

    data = data['data']
    questions = []

    print(data[0])
    for i in data:
        # print(i['question'])
        questions.append(i['question'])
        print(i['answer'])
        questions.append(i['answer'])
    return

from itertools import chain

def find_by_dict():
    import json

    s = ['วอลเลซ เสต็กเนอร์', 'เป็น']
    s.sort()
    fs = []
    for w in s:
        fs.append(w[0])

    fs = list(set(fs))
    print(fs)

    index_dir = 'E:/CPE#Y4/databaseTF/dict/'

    search = []
    for f in fs:

        file = open(index_dir + str(f) + ".json")
        data = json.load(file)

        for i in s:
            print(s)
            if (f == i[0]):
                s.remove(i)
                search.append(data[i])
    return

def plot_classify_graph():
    questions = [(2, 'เอเลียนส์'), (7, 'พระเจ้าอาฟองโซที่'), (13, 'เส้าเฟิง'), (4, 'กุลปราโมทย์ จิรประวัติ'),
                 (29, 'ชิงชัน'), (1133, 'แฝด'), (1, 'เชสเปเดส'), (1345, 'สมเด็จพระราชินีนาถ'), (10, 'คุณขา'),
                 (34, 'เสาวภา'), (922, 'ดวงใจ'), (4, 'แอนนา ฟาริส'), (2, 'หม่อมเจ้าประสพสุข'), (1, 'เฮเซเกียว'),
                 (1, 'กาลาตราบา บัลส์'), (15, 'ไอวีลีก'), (3, 'วัดเขาจีนแล'), (3, 'กราฟบน'), (9, 'ตั๊ก ศิริพร'),
                 (158, 'เต้ย'), (11, 'กันส์'), (10, 'ฮอลโลเวย์'), (86, 'แอตแลนติส'), (4, 'คาร์โรไลน์'),
                 (20, 'จังหวัดคา'), (104, 'ดร.'), (13, 'มายลิตเติ้ลโพนี่'), (5, 'เจ้าหญิงคลอทิลด์'), (9, 'ยอดมนู '),
                 (420, 'คราม'), (3088, 'เจ็ด'), (6, 'กร็องปาแล'), (1, 'ศาสตราจารย์ภาควิชาฟิสิกส์'), (1, 'ปิ่น เก็จมณี'),
                 (106, 'ไอก์'), (22, 'ประเทศกัวเตมา'), (101, 'นาอูรู'), (14, 'แมจิก'), (173, 'เอเชียแปซิฟิก'),
                 (6880, 'อะไร'), (37, 'คาบสมุทรจัตแลนด์'), (5, 'จงใจพระ'), (21, 'เอมี่ '), (10, 'อิงเหวิน'),
                 (19, 'เมืองลิสบอน'), (4, 'สะเออะ'), (3801, 'พี่น้อง'), (10, 'จรุงจิตต์'), (44, 'เจอร์'), (7, 'ไนน์มา'),
                 (116, 'กระทันหัน'), (104, 'พระเจ้าเล่าเสี้ยน'), (5, 'นิพัทธ์'), (13300, 'สโมสร'),
                 (937, 'ประเทศสิงคโปร์'), (96, 'อ่าวเบงกอล'), (878, 'ถนัด'), (634, 'เต๋า'), (1, 'พระยายุตราชา'),
                 (2, 'บริษัท ฮา ไม่จำกัด'), (35, 'แซ็กซัน'), (9, 'หาดเสือเต้น'), (1, 'นายแพทย์จักรีวัชร มหิดล'),
                 (5, 'กำลังกะเหรี่ยง'), (1, 'อิวานกา ทรัมป์'), (4, 'แอนนี ลีเบอวิตซ์'), (123, 'เบิร์ด ธงไชย'),
                 (354, 'ฉิน'), (2, 'พาราด๊อกซ์'), (3, 'แห่งเอเซีย'), (18339, 'ก่อตั้ง'), (287, 'ประเทศปานา'),
                 (1, 'ปู่ลี กุสลธโร'), (6, 'นายวิเชษฐ์ เกษมทองศรี'), (19, 'เขื่อนปากมูล'), (11, 'เยี่ย'),
                 (4, 'ท้าวศรีบุญเรือง'), (1, 'รัสเซียนพีระมิด'), (2, 'โทะชิอะกิ'), (16, 'เธมส์'), (8, 'ไซโจ'),
                 (5, 'เกียรติอรดี'), (48, 'กลมกล่อม'), (331, 'กลัด'), (2, 'กังซามาร์'), (1151, 'โฆษก'), (4, 'แซ็งเตมี'),
                 (8, 'พระครูพิศาลธรรมโกศล'), (6, 'จังหวัดใด'), (111, 'สุริยัน'), (3, 'พริ้งเกษมชัย'), (6, 'อำเภอสบ'),
                 (8, 'เรวิญานันท์ ทาเกิด'), (3, 'กูดฟิลลิง'), (5, 'ชาติโออาร์'), (2, 'นายแพทย์วิชัย ชัยจิตวณิชกุล'),
                 (10, 'ปภัสรา'), (2, 'ศาสตราจารย์ สม จาตุศรีพิทักษ์'), (5, 'ปีเตอร์ ดรักเกอร์'),
                 (69, 'เทือกเขาตะนาวศรี')]

    pprint(questions)
    plot = []
    for i in questions:
        plot.append(i[0])

    t = np.arange(100)
    plt.plot(t, plot, 'g')
    plt.plot(t, [3000] * 100, 'r')
    plt.plot(t, [10000] * 100, 'r')
    plt.show()
    return

def fill_tfidf():
    index_dir = 'E:\CPE#Y4\databaseTF\dict2\\'

    alphabet = 'ลห' # tf-idf at 'ล','ห' is not complete
    vowel = 'โ' # tf-idf at 'โ' is not complete
    e_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for f in vowel:
        file = index_dir + f +".json"
        print(file)
        data = json.load(open(file, mode = 'r' , encoding="utf-8-sig"))

        for k,v in data.items():
            for i in range(data[k].__len__()):
                if(data[k][i].__len__() != 5):
                    try:
                        data[k][i].append(data[k][i-1][4])
                    except IndexError:
                        print(k)
        json.dump(data, open(file, 'w'), ensure_ascii=True)
    return

for i in range(1000000):
    print(i,'/',1000000,end='\r')

