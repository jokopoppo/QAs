import editdistance

def normalized_edit_similarity(a, b):
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))

s = [ 'This is red car',
 'Red car is here',
 'This is not a blue car',
 'Blue or black car is here']

for i in s :
    print(normalized_edit_similarity('red car is this', i))