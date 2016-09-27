from gensim.models import ldamodel
from gensim import corpora
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle
import sys
import nltk

reload(sys)
sys.setdefaultencoding("utf-8")

documents = []
nTop = 20

file = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt'
f = open(file, "r")
papers = f.readlines()
for paper in papers:
	documents.append(paper)

print "corpus created"

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

texts = [[word for word in document.lower().split() if word not in stop] for document in documents]
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) < 10)
texts = [[word for word in text if word not in tokens_once] for text in texts]

print "stopwords and less frequent words removed"

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

print "Fitting...."
lda = ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=nTop, update_every=1, chunksize=1)
corpus_lda = lda[corpus]

f = "model" + str(nTop) + ".pkl"
pickle.dump(lda, open(f,"w"))

lda.show_topics()

