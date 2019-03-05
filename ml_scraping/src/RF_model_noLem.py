import nltk
import glob
import os
import random
import numpy as np 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation

DATA_DIR = "/Users/danielconway/thee-flying-chicken/ml_scraping/data/"
PROPORTION = 100
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
allowed_word_types = ["J", "R"]
lemmatizer = WordNetLemmatizer()

for r in negShort.split("\n"):
    documents.append( (r, 1) )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append( w[0].lower() )
for r in posShort.split("\n"):
    documents.append( (r, 0) )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append( w[0].lower() )
#neg_reviews = [r for r in neg.split("\n")]
#pos_reviews = [r for r in pos.split("\n")]

for r in negMovie:
    documents.append( (r, 1) )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append( w[0].lower() )

for r in posMovie:
    documents.append( (r, 0) )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append( w[0].lower() )
    

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
# save_word_features = open(os.path.join(DATA_DIR, "picked_algos", "WordFeatures.pickle"),"wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()
def find_features(document):
    words = word_tokenize(document)
    #lem_words = [lemmatizer.lemmatize(w) for w in words]
    features = []
    for w in word_features:
        features.append(w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]
 
random.shuffle(featuresets)
print(len(featuresets))
testing_set = featuresets[len(featuresets)//PROPORTION:]
training_set = featuresets[:len(featuresets)//PROPORTION]

x_train = [ x[0] for x in training_set]  
y_train = [ y[1] for y in training_set]

x_test = [ x[0] for x in testing_set]  
y_test = [ y[1] for y in testing_set]


# train RF

# train_test_spit --> https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
rfc = RandomForestClassifier(n_estimators=1000, n_jobs=-1, verbose=1)
rfc.fit(x_train, y_train)
print(classification_report(y_test, rfc.predict(x_test)))
#with open(os.path.join(DATA_DIR, "picked_algos", "RandomForestClassifier.pickle"),"wb") as f:
#    pickle.dump(clf, f)

svc = SVC(verbose=1)
svc.fit(x_train, y_train)
print(classification_report(y_test, svc.predict(x_test)))
#with open(os.path.join(DATA_DIR, "picked_algos", "SVCClassifier.pickle"),"wb") as f:
#    pickle.dump(clf, f)

lsvc = LinearSVC(verbose=1)
lsvc.fit(x_train, y_train)
print(classification_report(y_test, lsvc.predict(x_test)))
#with open(os.path.join(DATA_DIR, "picked_algos", "LinearSVCClassifier.pickle"),"wb") as f:
#    pickle.dump(clf, f)

nusvc = NuSVC(verbose=1)
nusvc.fit(x_train, y_train)
print(classification_report(y_test, nusvc.predict(x_test)))
#with open(os.path.join(DATA_DIR, "picked_algos", "NuSVCClassifier.pickle"),"wb") as f:
#    pickle.dump(clf, f)


# Evaluate RF



