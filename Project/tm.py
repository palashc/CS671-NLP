import lda, os
import numpy as np
import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

corpus = []

file = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt'
f = open(file, "r")
abstracts = f.readlines()
for abstract in abstracts:
	corpus.append(abstract)


# n_topics = 20
# n_top_words = 30
n_features = 1500

vectorizer = CountVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, stop_words = 'english')
matrix =  vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names()

vocab = feature_names

model = lda.LDA(n_topics=20, n_iter=1000, random_state=1)
model.fit(matrix)
topic_word = model.topic_word_
n_top_words = 20
 
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
