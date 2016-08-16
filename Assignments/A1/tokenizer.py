import libhfst
from sklearn.datasets import fetch_20newsgroups
import nltk



newsgroups_train = fetch_20newsgroups(subset='train')



t = nltk.word_tokenize(str(newsgroups_train.data[0]))
s = nltk.sent_tokenize(str(newsgroups_train.data[0]))

print t
print s

