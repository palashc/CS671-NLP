##############################create ai.txt, pi.txt#####################################################
# import os

# rootdir = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/extra"
# final = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/"
# num = 1

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         filepath = subdir + os.sep + file

#         if filepath.endswith(".txt"):
#             f = open(filepath,"r")
#             text = f.read()
#             a = text.find("ABSTRACT")
#             i = text.find("INTRODUCTION")
#             r = text.find("REFERENCES")
#             if a == -1:
#             	a = text.find("Abstract")
#             if i == -1:
#             	i = text.find("Introduction")
#             if r == -1:
#             	r = text.find("References")
#             if a == -1 or i == -1 or r ==-1 or i<=a or r<=i or r<=a:
#             	continue
#             abstract = text[a+8:i-1]
#             abstract = ''.join([k if ord(k) < 128 else ' ' for k in abstract])
#             paper = text[i+12:r-1]
#             paper = ''.join([k if ord(k) < 128 else ' ' for k in paper])
#             #print abstract
#             aFile = final + 'abstracts/a' + str(num) + ".txt"
#             pFile = final + 'papers/p' + str(num) + ".txt"
#             f = open(aFile, "w")
#             f.write(abstract)
#             f = open(pFile, "w")
#             f.write(paper)
#             f.close()
#             num += 1
#             print filepath, "00000000000"

	         
####################################################################################################

#################Finding average length of abstracts#############################################  -------> current average = 6.07
# total = 0

# import nltk,codecs
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# final = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/abstracts/"
# for i in range(1,1887):
# 	file = final + "a" + str(i) +".txt"
# 	f = open(file,"r")
# 	a = f.read()
# 	sent = nltk.sent_tokenize(a)
# 	total += len(sent)

# print total*1.0/1886
####################################################################################################

####################create ai.txt, pi.txt from original dataset#####################################
# import pandas as pd

# data = pd.read_csv('/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.csv')
# final = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/"
# # for row in data:
# # 	print row

# num = 1490

# for index, row in data.iterrows():
# 	a = row['Abstract']
# 	p = row['PaperText']
# 	i = p.find("INTRODUCTION")
# 	if i == -1:
# 		i = p.find("Introduction")
# 	if i == -1:
# 		continue
# 	r = p.find("REFERENCES")
# 	if r == -1:
# 		r = p.find("References")
# 	if r == -1:
# 		p = p[i+12:]
# 	else:
# 		p = p[i+12:r-1]
# 	aFile = final + 'abstracts/a' + str(num) + ".txt"
# 	pFile = final + 'papers/p' + str(num) + ".txt"
# 	f = open(aFile, "w")
# 	a = ''.join([k if ord(k) < 128 else ' ' for k in a])
# 	f.write(a)
# 	f = open(pFile, "w")
# 	p = ''.join([k if ord(k) < 128 else ' ' for k in p])
# 	f.write(p)
# 	f.close()
# 	num += 1

########################################################################################################

#####################create appended papers, abstracts file for topic model##############################
# final = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/"
# af = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Abstracts.txt"
# pf = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt"
# aff = open(af, "w")
# pff = open(pf, "w")

# for i in range(1,1887):
# 	file = final + "abstracts/a" + str(i) +".txt"
# 	f = open(file,"r")
# 	a = f.read()
# 	a = a.replace('\n', ' ').replace('\r', '').replace('1', '')
# 	aff.write(a + '\n')
# aff.close()

# for i in range(1,1887):
# 	file = final + "papers/p" + str(i) +".txt"
# 	f = open(file,"r")
# 	a = f.read()
# 	a = a.replace('\n', ' ').replace('\r', '')
# 	pff.write(a + '\n')
# pff.close()

##########################################################################################################


#################################Removing non ascii characters###############################################

# final = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/abstracts/"
# for i in range(1,1909):
# 	file = final + "a" + str(i) +".txt"
# 	f = open(file,"r+")
# 	a = f.read()
# 	a = ''.join([i if ord(i) < 128 else 'x' for i in a])
# 	f.write(a)

# fl = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/Papers.txt"
# f= open(fl,"r")
# f = f.read()
# for i in range(0,len(f)):
# 	if ord(f[i])>128:
# 		f[i] = ''


###################################################################################################
	