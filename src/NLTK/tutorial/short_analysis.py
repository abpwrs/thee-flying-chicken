import nltk
import pickle
import random
from nltk.classify.scikitlearn import SklearnClassifier
#from nltk.corpus import movie_reviews
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.tokenize import word_tokenize
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self.classifiers = classifiers
    def classify(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

short_pos = open("/Users/danielconway/thee-flying-chicken/src/NLTK/tutorial/short_reviews/positive.txt", "r").read()
short_neg = open("/Users/danielconway/thee-flying-chicken/src/NLTK/tutorial/short_reviews/negative.txt", "r").read()

documents = []
for r in short_pos.split("\n"):
    documents.append((r, "pos"))
for r in short_neg.split("\n"):
    documents.append((r, "neg"))

all_words = []
short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())
for w in short_neg_words:
    all_words.append(w.lower())

# word:frequency in order
all_words = nltk.FreqDist(all_words)
'''
# prints 15 most common words
print(all_words.most_common(15))
# prints # of occurences
print(all_words["stupid"])
'''
word_features = list(all_words.keys())[:5000]

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), catagory) for (rev,catagory) in documents]

random.shuffle(featuresets)

# if dissable random shuffle, if you only test against only one half, it will only test against pos or negative (fist and last half)
# 10,000 and something feature sets
training_set = featuresets[:10000]
testing_set = featuresets[10000:]

# posterior = prior occurences * likelyhood / current evidence
#classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Classifier Accuracy Percent: ", nltk.classify.accuracy(classifier, testing_set)*100 )
classifier.show_most_informative_features(15)
'''
### pickling ###
save_classifier = open("_name_.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

##loading##
pickle_in = open('_name_.pickle','rb')
new_variable = pickle.load(pickle_in)
'''
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
'''
GaussianNB_classifier = SklearnClassifier(GaussianNB())
GaussianNB_classifier.train(training_set)
print("GaussianNB_classifier accuracy percent:", (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)
'''
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier Accuracy Percent: ", nltk.classify.accuracy(BernoulliNB_classifier, testing_set)*100 )

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  SVC_classifier,
                                  LinearSVC_classifier,
                                  NuSVC_classifier)
print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
print("Classification: ", voted_classifier.classify(testing_set[0][0]), "Confidence %: " , voted_classifier.confidence(testing_set[0][0])*100)
print("Classification: ", voted_classifier.classify(testing_set[1][0]), "Confidence %: " , voted_classifier.confidence(testing_set[1][0])*100)
print("Classification: ", voted_classifier.classify(testing_set[2][0]), "Confidence %: " , voted_classifier.confidence(testing_set[2][0])*100)
print("Classification: ", voted_classifier.classify(testing_set[3][0]), "Confidence %: " , voted_classifier.confidence(testing_set[3][0])*100)
print("Classification: ", voted_classifier.classify(testing_set[4][0]), "Confidence %: " , voted_classifier.confidence(testing_set[4][0])*100)
print("Classification: ", voted_classifier.classify(testing_set[5][0]), "Confidence %: " , voted_classifier.confidence(testing_set[5][0])*100)


