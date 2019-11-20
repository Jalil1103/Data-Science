import nltk
import re
import matplotlib
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer


sample_text = state_union.raw("2005-GWBush.txt")
tain_text= state_union.raw("2004-GWBush.txt")

custom_sent_token = PunktSentenceTokenizer(sample_text)
custom = custom_sent_token.tokenize(tain_text)

def process():
    try:
        for i in custom:
            words = nltk.word_tokenize(i)
            tag = nltk.pos_tag(words)
            named = nltk.ne_chunk(tag, binary = False)


    except Exception as e:
        print(str(e))

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize(""))