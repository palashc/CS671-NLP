import pickle
from sklearn.svm import LinearSVC
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn import cross_validation

f = open("train.pkl","rb")
features = pickle.load(f)
f.close()

f = open("train_label.pkl","rb")
labels = pickle.load(f)
f.close()

print "data loaded..."

classifier = LinearSVC()

p = 0.7*len(features)
p = int(p)
print p
trainF = features[:p]
trainL = labels[:p]
testF = features[p:]
testL = labels[p:]

classifier.fit(trainF, trainL)

pred = classifier.predict(testF)

A = accuracy_score(testL, pred)
print "Accuracy: ", A


