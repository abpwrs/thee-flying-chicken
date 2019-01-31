import nltk
import glob
import os
import random
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation

DATA_DIR = "/Users/danielconway/thee-flying-chicken/ml_scraping/data/"

# update your branch:
# git checkout master
# git pull
# git checkout dc
# git merge master
# git stash
# do above commands
# git stash pop
# mv thee-flying-chicken/src/* thee-flying-chicken/ml_scraping/src/
# cd ml_scraping 
# git reset HEAD
# cd ml_scraping/data
# tar -xzvf *.tar.gz

negMovie = []
posMovie = []
for f_name in glob.glob(os.path.join(DATA_DIR,"movie_reviews","neg","*")):
    negMovie.append(open(f_name, 'r').read())

for f_name in glob.glob(os.path.join(DATA_DIR,"movie_reviews", "pos", "*")):
    posMovie.append(open(f_name,'r').read())

    

negShort = open(os.path.join(DATA_DIR, "pos_neg_data", "neg.txt"), 'r').read()
posShort = open(os.path.join(DATA_DIR, "pos_neg_data", "pos.txt"), 'r').read()

documents = []
all_words = []
#  j is adjective, r is adverb, and v is verb
allowed_word_types = ["J"]
lemmatizer = WordNetLemmatizer()

for r in negShort.split("\n"):
    documents.append( (r, "neg") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(lemmatizer.lemmatize( w[0].lower()) )
for r in posShort.split("\n"):
    documents.append( (r, "pos") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(lemmatizer.lemmatize( w[0].lower()) )
#neg_reviews = [r for r in neg.split("\n")]
#pos_reviews = [r for r in pos.split("\n")]

for r in negMovie:
    documents.append( (r, "neg") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(lemmatizer.lemmatize( w[0].lower()) )

for r in posMovie:
    documents.append( (r, "pos") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(lemmatizer.lemmatize( w[0].lower()) )
    

# save_word_features = open(glob.glob(os.path.join(DATA_DIR,"pickled_algos", "word_features20%.pickle","wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()
'''
[pos_reviews.append(r) for r in posMovie]
[neg_reviews.append(r) for r in negMovie]

# tokenize pos & neg reviews
tokenized_pos = [(word_tokenize(r)) for r in pos_reviews]
tokenized_neg = [(word_tokenize(r)) for r in neg_reviews]
pos_pos = nltk.pos_tag(tokenized_pos)
pos_neg = nltk.pos_tag(tokenized_neg)



# remove stop words
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# lemmatize pos & neg reviews
lematized_pos = [[lemmatizer.lemmatize(word) for word in sentence if word not in stop_words and word not in punctuation] for sentence in pos_pos]
lematized_neg = [[lemmatizer.lemmatize(word) for word in sentence if word not in stop_words and word not in punctuation] for sentence in pos_neg]
#print(lematized_neg[:2])
'''
# bag of words all data
# 20%
'''
arr_one = np.array(lematized_pos).flatten()
arr_two = np.array(lematized_neg).flatten()
combined = []
def add(text):
    if type(text) != str:
        for l in text:
            add(l)
    else:
        combined.append(text)

add(arr_one)
add(arr_two)
'''
# number of unique words
all_words = nltk.FreqDist(all_words)
word_features = list( all_words.keys() )[:len(all_words.keys())//5 ]
# save_word_features = open("pickled_algos/word_features5k.pickle","wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[lemmatizer.lemmatize(w)] = (w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]
 
random.shuffle(featuresets)
print(len(featuresets))
testing_set = featuresets[len(featuresets)//100:]
training_set = featuresets[:len(featuresets)//100]


# train RF

# train_test_spit --> https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
#clf = RandomForestClassifier()
#clf.fit(x_train, y_train)
RandomForestClassifier = SklearnClassifier(RandomForestClassifier())
RandomForestClassifier.train(training_set)
print("Random Forest classifier accuracy percent:", (nltk.classify.accuracy(RandomForestClassifier, testing_set))*100)
# save_classifier = open("os.path.join(DATA_DIR, "picked_algos", "RandomForestClassifier.pickle")","wb")
# pickle.dump(BernoulliNB_classifier, save_classifier)
# save_classifier.close()

# print(classification_report(y_test, clf.predict(x_test)))

# Evaluate RF



