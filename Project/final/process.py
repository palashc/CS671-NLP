import os, pickle, collections, nltk
from scipy import spatial
import heapq
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
stop = set(nltk.corpus.stopwords.words('english'))
#result = 1 - spatial.distance.cosine(model[w], googleW2V[w])

# root = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/papers/'

# paperFile = open("/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt", "w")

# for file in os.listdir(root):
# 	path = root + file
# 	f = open(path, "r")
# 	paper = f.read()
# 	paperFile.write(paper.replace('\n', ' ').replace('\r', ''))
# 	paperFile.write('\n')

paperPath = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/papers/'
abstractPath = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/abstracts/'

clusterMap = pickle.load(open("ClusterMap.pkl", "r"))

featureVecs = []
labels = []

def getDict(words):
    '''Return frequency (count) for each token in the text'''
    frequencies = collections.defaultdict(int)
    for token in words:
        frequencies[token] += 1

    return frequencies

def getVec(w):
	count = 0
	vec = np.zeros(50, dtype="float32" )
	
	for word in w:
		if word in clusterMap:
			index = clusterMap[word]
			vec[index] += 1
			count += 1

	return np.divide(vec, count + 1)


def getFeatureLabel(paperSents, abstractSents):       #len, position, ratio-thematic#
	temp = []
	finalVecs = []
	lbl = []
	for sent in abstractSents:
		ws = nltk.word_tokenize(sent)
		ws = [w for w in ws if w not in stop]
		temp.extend(ws)
	absractVec = getVec(temp)

	temp = []
	for sent in paperSents:
		ws = nltk.word_tokenize(sent)
		ws = [w for w in ws if w not in stop]
		temp.extend(ws)
	paperDict = getDict(temp)
	NumContentWords = len(paperDict)
	thematicWords = heapq.nlargest(10, paperDict)
	DocLen = len(paperSents)

	scores = []

	for i in range(len(paperSents)):
		fvec = []
		words = nltk.word_tokenize(paperSents[i])
		fvec.append(len(words))
		words = [word for word in words if word not in stop]
		paperVec = getVec(words)
		score = 1 - spatial.distance.cosine(absractVec, paperVec)
		scores.append(score)
		fvec.append(DocLen*1.0/(i+1))
		them = [w for w in words if w in thematicWords]
		fvec.append(len(them)*1.0/(NumContentWords + 1))
		finalVecs.append(fvec)

	maxScore = max(scores)
	for score in scores:
		if score > 0.65*maxScore:
			lbl.append(1)
		else:
			lbl.append(-1)

	return finalVecs, lbl

		
i = 0 
testfiles = []
for file in os.listdir(paperPath):
	if i > 1300:
		testfiles.append(file)
	print file
	ppr = paperPath + file
	abstrct = abstractPath + file.replace('p', 'a')
	paper = open(ppr, "r").read().lower()
	abstract = open(abstrct, "r").read().lower()
	paperSents = nltk.sent_tokenize(paper)
	abstractSents = nltk.sent_tokenize(abstract)
	vec, l = getFeatureLabel(paperSents, abstractSents)
	i += 1
	featureVecs.extend(vec)
	labels.extend(l)


pickle.dump(testfiles, open("testfiles.pkl", "w"))
pickle.dump(featureVecs, open("features.pkl", "w"))
pickle.dump(labels, open("labels.pkl", "w"))