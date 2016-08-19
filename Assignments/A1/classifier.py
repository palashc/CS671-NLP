import libhfst
from sklearn.datasets import fetch_20newsgroups
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import sys

def getAc(pred, test):
	correct = 0
	for i in range(0,len(test)):
		if pred[i] == test[i]:
			correct += 1
	return correct*1.0/len(test)


reload(sys)
sys.setdefaultencoding("utf-8")


#fetch dataset
newsgroups_train = fetch_20newsgroups(subset='train')
#newsgroups_train.data = newsgroups_train.data[:4000]    #reduce time for now
newsgroups_test = fetch_20newsgroups(subset='test')
#newsgroups_test.data = newsgroups_test.data[:100]
vec = DictVectorizer()

features = []
window_dicts = []

training_labels = []
testing_labels = []

classifier = LinearSVC()
k = 0
#training data
print "Creating feature vectors"
print "Total training files: ",len(newsgroups_train.data)
for j in range(0,len(newsgroups_train.data)): 
	newsgroups_train.data[j] = "START " + "START " + newsgroups_train.data[j].rstrip() + " STOP " + "STOP"  #append start,stop tokens
	t = nltk.word_tokenize(newsgroups_train.data[j].encode('utf-8'))  #tokenize
	tags = nltk.pos_tag(t)                                            #get tags
 	tags = dict(tags)
	for i in range(2,len(t)-3): 
		k += 1                                      #take context window of size 5
		window = {"word-2": t[i-2], "tag-2": tags[t[i-2]], "word-1": t[i-1], "tag-1": tags[t[i-1]], "word+1": t[i+1], "tag+1": tags[t[i+1]], "word+2": t[i+2], "tag+2": tags[t[i+2]], }
		#features.append(vec.fit_transform(window).toarray()[0])           #make dict and vectorize
		window_dicts.append(window)
		if t[i] == '.':
			training_labels.append(1)
		else:
			training_labels.append(0)
print "Total testing files: ",len(newsgroups_test.data)
l = 0
for j in range(0,len(newsgroups_test.data)): 
	newsgroups_test.data[j] = "START " + "START " + newsgroups_train.data[j].rstrip() + " STOP " + "STOP"
	t = nltk.word_tokenize(newsgroups_test.data[j].encode('utf-8'))
	tags = nltk.pos_tag(t)
 	tags = dict(tags)
	for i in range(2,len(t)-3):
		l += 1
		window = {"word-2": t[i-2], "tag-2": tags[t[i-2]], "word-1": t[i-1], "tag-1": tags[t[i-1]], "word+1": t[i+1], "tag+1": tags[t[i+1]], "word+2": t[i+2], "tag+2": tags[t[i+2]], }
		window_dicts.append(window)
		if t[i] == '.':
			testing_labels.append(1)
		else:
			testing_labels.append(0)

features = vec.fit_transform(window_dicts)

transformer = TfidfTransformer()
transformed = transformer.fit_transform(features)

train = transformed[:k,:]
test = transformed[k:,:]

print "Training..."
classifier.fit(train, training_labels)

print "Testing..."
prediction = classifier.predict(test)
# if prediction == 1:
# 	print "Sentence terminator detected in: "
# 	print testing_dicts[i]['word-2'] + " " + testing_dicts[i]['word-1'] + " " + testing_dicts[i]['word+1'] + " " + testing_dicts[i]['word+2']

print "Accuracy: ", getAc(prediction, testing_labels)