
def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

def normalized_edit_similarity(a, b):
    import editdistance
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

print(similar('สุเทพ เทือกสุบรรณ','ภรรยาสุเทพ เทือกสุบรรณ'))
print(similar('สุเทพ เทือกสุบรรณ','สุเทพ เทือกสุบรรณ'))

print(normalized_edit_similarity('สุเทพ เทือกสุบรรณ','ภรรยาสุเทพ เทือกสุบรรณ'))
print(normalized_edit_similarity('สุเทพ เทือกสุบรรณ','สุเทพ เทือกสุบรรณ'))