import pickle
from sklearn.svm import LinearSVC
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

f = open("features.pkl","rb")
features = pickle.load(f)
f.close()

f = open("labels.pkl","rb")
labels = pickle.load(f)
f.close()

print "data loaded..."

classifier = LinearSVC()
#classifier = RandomForestClassifier(n_estimators=500)
# classifiers = [
#     DecisionTreeClassifier(max_depth=5),
#     RandomForestClassifier(max_depth=5, n_estimators=100, max_features=1),
#     AdaBoostClassifier(),
#     GaussianNB(),
#     QuadraticDiscriminantAnalysis()]

p = 0.7*len(features)
p = int(p)
print p
trainF = features[:p]
trainL = labels[:p]
testF = features[p:]
testL = labels[p:]



X = classifier.fit(trainF, trainL)

pickle.dump(X, open("classifier.pkl", "w"))


pred = classifier.predict(testF)

A = accuracy_score(testL, pred)
print "Accuracy: ", A


