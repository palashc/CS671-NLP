import nltk, os
import pprint, re, sklearn,sys
import numpy as np
from pprint import pprint 
import pickle, tokenizer, segmenter


def sentTokenizer(str):
	#return nltk.sent_tokenize(str)
	return segmenter.mySentSeg(str)
	


def wordTokenizer(str):
	#return nltk.word_tokenize(str)
	return tokenizer.myTokenizer(str)



if __name__ == "__main__":
	PATH =  os.path.abspath('parsing.py')  #to create feature vectors in directory of dataset
	PATH = PATH[:-10]
	dirlist = os.listdir(PATH)
	str1 = ''
	for itr in dirlist:
		str1 += itr + '/*' + ' '
	print str1
	cmd = 'cat ' + str1 + '> data.txt'
	os.system(cmd)
	with open('data.txt','r') as myfile:
		data = myfile.read()

	
	data = unicode(data, errors='ignore')
	sent = sentTokenizer(data)

	data2 = data
	print len(sent)
	listOfFeatures = []
	count = 0
	ind = 0
	periodsList = []
 	
	#bag of ascii value
 	g = [-2]*128
	g[65:91] = [-1]*26
	g[9] = 0
	g[10] = 0
	g[32] = 0
	g[46] = 1
	g[33] = 1
	g[63] = 1
	g[48:58] = [2]*10
	g[97:123] = [3]*26
	
	##positive samples

	for i in sent:
		i = i.rstrip()
		count += 1
		if i[-1] == '.':
			try:
				index = data2.index(i, ind+1)
				index = index + len(i) - 1
				k = index
				ind = k
				periodsList.append(k)
				feature = data2[k-3:k] + data2[k+1:k+4]	#taking neighbouring 5 chars around period as features
				listOfFeatures.append(feature)
			except:
				print(i)

	data2 = data
	count = 0
	ind = 0
	n_periods = 0


	#negative samples

	listOfFeatures2 = []
	print len(data2)
	for i in range(0,len(data2)):
		if data2[i] == '.':
			if n_periods < len(periodsList) and i == periodsList[n_periods]:
				n_periods += 1
					
			else:
				listOfFeatures2.append(data2[i-3:i] + data2[i+1:i+4])	#taking neighbouring 3 characters on both sides as features



	#create bag of ascii value feature vector
	pos_Feat = []
	for i in listOfFeatures:
		tmp = []
		for j in range(0,6):
			tmp.append(g[ord(i[j])])
		pos_Feat.append(tmp)

	neg_Feat = []
	for i in listOfFeatures2:
		tmp = []
		for j in range(0,6):
			tmp.append(g[ord(i[j])])
		neg_Feat.append(tmp)


	len1 = len(pos_Feat)
	len2 = len(neg_Feat)
	print len1,len2
	cls = [1]*len1 + [2]*len2
	totalDataset = pos_Feat + neg_Feat

	#dump data
	with open('train.pkl', 'wb') as f:		#features of dataset
		pickle.dump(totalDataset, f)

	with open('train_label.pkl', 'wb') as f:	#labels of dataset
		pickle.dump(cls, f)



	