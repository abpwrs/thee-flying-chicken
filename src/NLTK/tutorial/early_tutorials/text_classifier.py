import nltk
import pickle
import random
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.corpus import movie_reviews
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

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


'''
categories are pos or neg.
for each unique file id, the text is put into a list of words
'''
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories() 
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
# word:frequency in order
all_words = nltk.FreqDist(all_words)
'''
# prints 15 most common words
print(all_words.most_common(15))
# prints # of occurences
print(all_words["stupid"])
'''
word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), catagory) for (rev,catagory) in documents]

# if dissable random shuffle, if you only test against only one half, it will only test against pos or negative (fist and last half)
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# posterior = prior occurences * likelyhood / current evidence
#classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Original Naive Bayes Classifier Accuracy Percent: ", nltk.classify.accuracy(classifier, testing_set)*100 )
classifier.show_most_informative_features(15)

'''
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
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


