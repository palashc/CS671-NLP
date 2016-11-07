from gensim.models import word2vec
import nltk, pickle, logging
from sklearn.cluster import MiniBatchKMeans

stop = set(nltk.corpus.stopwords.words('english'))

corpusFilePath = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Abstracts.txt"
corpusFilePath1 = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt"

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = open(corpusFilePath, "r")
abstracts = f.readlines()

f1 = open(corpusFilePath1, "r")
papers = f.readlines()
sents = []

for abstract in abstracts:
	abstract = abstract.lower()
	sent = nltk.sent_tokenize(abstract)
	for s in sent:
		words = nltk.word_tokenize(s)
		words = [word for word in words if word not in stop]
		sents.append(words)

for paper in papers:
	paper = paper.lower()
	sent = nltk.sent_tokenize(paper)
	for s in sent:
		words = nltk.word_tokenize(s)
		words = [word for word in words if word not in stop]
		sents.append(words)

model = word2vec.Word2Vec(sents, workers=4, size=300, min_count = 0, window = 10, seed=200)
model.save("word-vecs.txt")

model = word2vec.Word2Vec.load("word-vecs.txt")

word_vectors = model.syn0

num_clusters = 50

kmeans_clustering = MiniBatchKMeans( n_clusters = num_clusters )
print "getting clusters.."
idx = kmeans_clustering.fit_predict( word_vectors )

print 'getting map...'
word_centroid_map = dict(zip( model.index2word, idx ))


print 'dumping..'
pickle.dump(word_centroid_map, open("ClusterMap.pkl", "w"))


