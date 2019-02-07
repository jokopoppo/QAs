
def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

classes = ['ใคร', 'ว่า อะไร', 'ประเทศ อะไร', 'จังหวัด อะไร', 'เมือง อะไร' , 'ประเทศ ใด', 'จังหวัด ใด', 'เมือง ใด' ,'คน ใด'
           , 'เมื่อ ใด', 'เวลา ใด', 'ภาค ใด', 'แคว้น ใด', 'ที่ ใด', 'ที่ ไหน', 'เท่า ไร', 'เมื่อ ไร', 'อย่าง ไร', 'ชื่อ อะไร', 'ปี อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'other ใด', 'other อะไร']
question_type = [['กี่', 'ปี ใด', 'ปี อะไร', 'พ.ศ.  อะไร', 'ค.ศ.  อะไร', 'พ.ศ. อะไร', 'ค.ศ. อะไร', 'พ.ศ. ใด', 'พ.ศ.  ใด', 'ค.ศ. ใด', 'ค.ศ.  ใด', 'เท่า ไร', 'เท่า ไหร่', 'เท่า ใด']
                 ,['ใคร', 'ว่า อะไร', 'ชื่อ อะไร', 'คน ใด']
                 ,['ประเทศ ใด', 'ประเทศ อะไร']
                 ,['จังหวัด ใด', 'จังหวัด อะไร']
                 ,['เมือง ใด', 'เมือง อะไร']]

c = []
for i in question_type:
    for j in i:
        c.append(j)

print(set(classes) - set(c))