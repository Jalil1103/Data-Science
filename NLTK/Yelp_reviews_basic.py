
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup

#Url calling for the yelp page of Grange#
sauce = 'https://www.yelp.com/biz/grange-insurance-companies-columbus-5'

# Requesting the webpage
r = requests.get(sauce)
#Turning the request into a text file for preparing for analysis
html_doc = r.text

#Cleaning the text file into structured HTML page
soup = BeautifulSoup(html_doc, "html.parser")
p_tags = soup.find_all("p")

for text in p_tags:
    yelp_reviews = open("yelp_reviews.txt", 'a')
    texts = text.get_text()
    yelp_reviews.write(texts)
    yelp_reviews.write('\n')
    yelp_reviews.close()

#Not yet done function
def text_processing(text):
    p_tags = soup.find_all("p")
    for text in p_tags:
        review = open(text, 'a')
        words = text.get_text()
        review.write(text)
        review.write('\n')
        review.close()
    return review
        


# In[3]:

#Importing the libararies needed for ML
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.tokenize import word_tokenize
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode


# In[4]:

#Empty list to store values in
all_words = []

#Getting our text file of yelp reviews
reviews = open("C:/Users/Adini/Desktop/reviews/yelp_reviews.txt").read()
file= reviews.split(" ")

#processing our file for Sentiment Analysis
for line in file:
    all_words.append(line)
    
all_words = nltk.FreqDist(all_words)
stopwords = nltk.corpus.stopwords.words('english')
new_words = nltk.FreqDist(w.lower() for w in all_words if w not in stopwords)
word_features = list(new_words.keys())[:3000]


# In[5]:

#finding features from our text files
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#Importing movie reviews which are preprocessed as either negative or positive in the document variable
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#Since they are in order we shuffle them to have a more accurate ML 
random.shuffle(documents)
featuresets = [(find_features(rev), category) for (rev, category) in documents]


#Creating training set and a testing set for our ML model
training_set = featuresets[:1900]
testing_set= featuresets[1900:]



# In[10]:

#Training and Testing our ML model for sentiment analysis
classifier = nltk.NaiveBayesClassifier.train(training_set)
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent:",nltk.classify.accuracy(SGDC_classifier, testing_set)*100)


#printing how accurate we were with the model
# Simple Naive Bayes wasn't as accurate as we would like for a classifier and we can further apply other models for more accuracy
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
print(classifier.show_most_informative_features(10))






# In[7]:

#Saving our ML model for easy use later as pickled file
naive_bayes = open("naivebayes.pickle", "wb")
pickle.dump(classifier,naive_bayes)
naive_bayes.close()


# In[ ]:



