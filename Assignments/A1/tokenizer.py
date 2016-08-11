import libhfst
from sklearn.datasets import fetch_20newsgroups



newsgroups_train = fetch_20newsgroups(subset='train')



myTokenizer = libhfst.HfstTokenizer()

fp = open("vocabulary.txt", "r")

words = fp.readlines()

for i in range(len(words)):
	myTokenizer.add_multichar_symbol(words[i].rstrip())
	

fp.close()


myTokenizer.add_skip_symbol('.')
myTokenizer.add_skip_symbol(' ')
myTokenizer.add_skip_symbol('-')
myTokenizer.add_skip_symbol(',')
myTokenizer.add_skip_symbol('\n')


t = myTokenizer.tokenize_one_level(str(newsgroups_train.data[0]))

print t

