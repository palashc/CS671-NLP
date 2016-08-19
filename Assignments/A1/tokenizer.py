import lex

def myTokenizer(data):
	tokens = (
	   'NUMBER',
	   'WORD',
	   'PUNCTUATION'
	)
	t_NUMBER    = r'[0-9]+'
	t_WORD   = r'[a-zA-Z_]+'
	t_PUNCTUATION=r'\+|\-|\*|\!|\@|\#|\$|\%|\^|\&|\(|\)|\_|\=|\~|\`|\{|\[|\]|\}|\}|\\|\||\:|\;|\"|\'|\<|\>|\,|\.|\/|\?'
	t_ignore  = ' \t\n'

	def t_error(t):
	    #print("Illegal character '%s'" % t.value[0])
	    t.lexer.skip(1)
	
	lexer = lex.lex()
	lexer.input(data)

	tokens = []
	
	while True:
	    tok = lexer.token()
	    if not tok: 
	        break      
	    tokens.append(str(tok.value))

	return tokens