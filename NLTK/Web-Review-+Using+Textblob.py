
# coding: utf-8

# In[43]:

from textblob import TextBlob
import nltk
from textblob.classifiers import NaiveBayesClassifier
import random


# In[38]:

#getting positve and negative reviews to train the ML algorithms#
positive = open('C:\\Users\Adini\Desktop\positive.txt','r').read()
negative = open('C:/Users/Adini/Desktop/negative.txt','r').read()


# In[ ]:

#Creating an empty list to store values
documents = []
all_words = []
# Allowed word types just contains "J" being adjectives 
allowed_word_types = ["J"]
# Appending postive 
for r in positive.split('\n'):
    document.append((r, "pos"))
#Appending Negative
for r in negative.split('\n'):
    document.append((r, "neg"))
    
for p in positive.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

    
for p in negative.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())



# In[ ]:

training_set = documents[:10000]
testing_set =  documents[10000:]
cl = NaiveBayesClassifier(training_set)


# In[ ]:



