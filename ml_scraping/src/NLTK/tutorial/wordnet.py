from nltk.corpus import wordnet
'''
syns = wordnet.synsets("program")
print(syns)

# synset example
print(syns[0].name())

# word lemmas
print(syns[0].lemmas())

# just the word
print(syns[0].lemmas()[0].name())

# defintion of first synset
print(syns[0].definition())

# examples of word
print(syns[0].examples())
'''
'''
synonyms = []
antonyms = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print("l: ", l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))
'''

### similarity ###
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
# Wu and Palmer method - returns percent
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2))