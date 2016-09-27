import pickle
from gensim import corpora
from nltk.corpus import stopwords
import nltk
from scipy import spatial
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
stop = set(stopwords.words('english'))
D = 1908

def convert2vec(LoT):
	ans = [0]*20
	for key,value in LoT:
		ans[key] = value
	return ans

model = pickle.load(open("model20.pkl","r"))

finalP = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/papers/"
finalA = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/attempt1/"

def generateAbstract(filepath):
	paper = []
	f = open(filepath,"r");
	paper.append(f.read())
	f.close()
	paper[0] = ''.join([i if ord(i) < 128 else ' ' for i in paper[0]])
	candidates = nltk.sent_tokenize(paper[0])
	total = paper + candidates
	texts = [[word for word in document.lower().split() if word not in stop] for document in total]
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	topicVectors = model[corpus]
	paperTV = convert2vec(topicVectors[0])
	scores = []
	topicVectors = topicVectors[1:]
	for i in range(0,len(topicVectors)):
		t = convert2vec(topicVectors[i])
		score = 1 - spatial.distance.cosine(paperTV, t)
		scores.append((i,score))
	sort = sorted(scores, key=lambda tup: tup[1])
	count = 0
	abstract = ""
	for i in range(0,len(sort)):
		index,score = sort[i]
		abstract += candidates[index]
		count += 1
		if count==8:
			break

	return abstract


for num in range(1,D+1):
	print num
	pFile = finalP + "p" + str(num) + ".txt"
	try:
		a = generateAbstract(pFile)
	except:
		continue
	aFile = finalA + "a" + str(num) + ".txt"
	f1 = open(aFile, "w")
	f1.write(a)
	f1.close()
	







