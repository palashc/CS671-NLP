import os, pickle, collections, nltk
from scipy import spatial
import heapq
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
stop = set(nltk.corpus.stopwords.words('english'))

paperPath = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/papers/'
abstractPath = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/abstracts/'

f = open("testfiles.pkl","rb")
testfiles = pickle.load(f)
f.close()