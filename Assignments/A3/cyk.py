'''
~cyk.py~
Author: Palash Chauhan
Last Modified: 25th October, 2016

Takes as input a grammar in the CNF form and a string
and outputs whether the string can be generated from
the grammar or not. If it can be, the parse tree is
also returned as a nested list
'''


def readGrammar(filename):
	#read grammar
	grammar = []
	f = open(filename,"r")
	Rs = f.readlines()
	for r in Rs:
		rule = {}
		r = r.split('->')
		r[1] = r[1].split('|')
		for i in range(0,len(r[1])):
			r[1][i] = r[1][i].rstrip()
			grammar.append({'lhs':r[0].rstrip(), 'rhs':tuple(r[1][i].split(" "))})
	return grammar


def checkRHS(s, grammar):
	ans = [rule['lhs'] for rule in grammar if tuple(s) == rule['rhs']]
	return ans

def checkRHS2(combo, grammar):
	ans = []
	for c in combo:
		for rule in grammar:
			if rule['rhs']==c:
				ans.append(rule['lhs'])
	return ans

def initTable(s, grammar):
	numTokens = len(s)
	matrix =  [[ [] for i in range(numTokens+1)] for j in range(numTokens+1)]
	for i in range(numTokens):
		matrix[i][i+1] = checkRHS(s[i], grammar)
	return matrix

def display(matrix, s):
	print '\nTable ' + ' '.join([("%-4d" % i) for i in range(1, len(matrix))])
	for i in range(len(matrix)-1):
		print "%d " % i,
		for j in range(1, len(matrix)):
				print "%-4s" % matrix[i][j],
		print

def genComb(l1,l2):
	ans = []
	for i in l1:
		for j in l2:
			ans.append((i,j))
	return ans

def completeTable(matrix,grammar, s, trace=False):
	index = {} #reverse lookup
	# for rule in grammar:
	# 	index[rule['rhs']] = rule['lhs']
	numTokens = len(s)
	for span in range(2, numTokens+1):
		for start in range(numTokens+1-span): #go down diagonal
			end = start + span
			for mid in range(start+1, end):
				nt1, nt2 = matrix[start][mid], matrix[mid][end]
				combo = genComb(nt1, nt2)
				res = checkRHS2(combo, grammar)
				if res:
					matrix[start][end].extend(res)


	return matrix




grammar = readGrammar('test_grammar.txt')
startSymbol = grammar[0]['lhs']
#print grammar

testString = raw_input("Enter string to be checked: \n")
#testString = 'aaaaaaab'



matrix = initTable(testString, grammar)

matrix1 = completeTable(matrix, grammar, testString, False)

#display(matrix1,testString)

if startSymbol in matrix1[0][len(testString)]:
	print "Yes"
else:
	print "NO"