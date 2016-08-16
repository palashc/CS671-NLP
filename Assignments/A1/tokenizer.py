import libhfst
from sklearn.datasets import fetch_20newsgroups
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *



newsgroups_train = fetch_20newsgroups(subset='train')



t = nltk.word_tokenize(str(newsgroups_train.data[0]))

# s = nltk.sent_tokenize(str(newsgroups_train.data[0]))

tags = nltk.pos_tag(t)
tags = dict(tags)
# print t
# print s
# print tags

WNL = WordNetLemmatizer()
porter_stemmer = PorterStemmer()
for word in t:
	print word + " ---> " + WNL.lemmatize(word) + " ---> " + porter_stemmer.stem(word) + " ---> " + tags[word]

