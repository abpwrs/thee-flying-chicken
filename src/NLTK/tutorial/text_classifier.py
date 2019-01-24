import nltk
import random
from nltk.corpus import movie_reviews

'''
categories are pos or neg.
'''
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories() 
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#prints 15 most common words
print(all_words.most_common(15))
#prints # of occurences
print(all_words["stupid"])