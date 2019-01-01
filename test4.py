from pythainlp.corpus import wordnet

all = ['ควาย','โง่','อินทรี']

for s in all :
    synonyms = []
    for syn in wordnet.synsets(s) :
        for word in syn.lemma_names('tha'):
            synonyms.append(word)

    synonyms=list(set(synonyms))
    print(synonyms)

