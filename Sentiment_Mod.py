
# coding: utf-8

# ## Importing the required Libraries 

# In[3]:


import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


# ## Defining Class for vote classifier 

# In[7]:


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


# ## Load all our pickled algos and data

# In[20]:


algo = open("documents.pickle","rb")
documents = pickle.load(algo)
algo.close()

algo = open("features.pickle","rb")
word_features = pickle.load(algo)
algo.close()

algo = open("naivebayes.pickle","rb")
classifier = pickle.load(algo)
algo.close()

algo = open("Bernouli.pickle","rb")
BernoulliNB_classifier = pickle.load(algo)
algo.close()

algo = open("LogisticRegression.pickle","rb")
LogisticRegression_classifier = pickle.load(algo)
algo.close()

algo = open("SGDClassifier.pickle","rb")
SDGClassifier_classifier = pickle.load(algo)
algo.close()

algo = open("MNB.pickle","rb")
MNB_classifier = pickle.load(algo)
algo.close()

algo = open("NuSVC.pickle","rb")
NuSVC_classifier = pickle.load(algo)
algo.close()

algo = open("SVC.pickle","rb")
SVC_classifier = pickle.load(algo)
algo.close()

algo = open("LinearSVC.pickle","rb")
LinearSVC_classifier = pickle.load(algo)
algo.close()


# ## Defining Featuresets function 

# In[15]:


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# ## Voting classifier 

# In[21]:


voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)


# ## Defining module function to call 

# In[22]:


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats), voted_classifier.confidence(feats)

