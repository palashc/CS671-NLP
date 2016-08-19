import lex

def mySentSeg(data)
	tokens = (
	   'SENT1',
	   'SENT2'
	)
	t_SENT1    = r'([^.!?]|\.[^\s\t])*(\!|\?|\.\.\.|\.[\s\t]|\.$)'
	t_SENT2  = r'([^.!?]|\.[^\s\t])+'
	
	def t_error(t):
	    #print("Illegal character '%s'" % t.value[0])
	    t.lexer.skip(1)

	lexer = lex.lex()
	lexer.input(data)
	sent = []
	
	while True:
	    tok = lexer.token()
	    if not tok: 
	        break      
	    sent.append(str(tok.value))

	return sent