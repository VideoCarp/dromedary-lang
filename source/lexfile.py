def analyze(toparse=None):
    if toparse is None:
       raise Exception("Lexer did not get enough info.")
    print("Successfully entered lexical analyzer.")
    data = toparse
    result = []
    lexed = []
    lexdata = []
    datawords = data.split(" ")
    lines = data.split("\n")
    class Lexicon:
        SYMBOLS = {
            '-': 'SUBTRACT',
            '+': 'PLUS',
            '*': 'MULTIPLY',
            '%': 'MODULUS',
            '/': 'DIVIDE',
            '(': 'RPAREN',
            ')': 'LPAREN',
            '[': 'RBRACKET',
            ']': 'LBRACKET',
            '{': 'RBRACE',
            '}': 'LBRACE',
            '=': 'REASSIGN',
            ':=': 'ASSIGN',
            '==': 'EQUIVALENT',
            '!=': 'UNEQUAL',
            '>': 'GREATER',
            '<': 'SMALLER',
            '>=': 'GREATER_OR_EQUAL',
            '<=': 'SMALLER_OR_EQUAL',
            ',': 'COMMA'
        }
        KEYWORDS = {
            'if': 'FLOW_IF',
            'while': 'FLOW_WHILE',
            'for': 'FLOW_FOR',
            'function': 'ASSIGN_FUNCTION',
            'in': 'IN_OPERATOR',
            'true': 'BOOL_TRUE',
            'false': 'BOOL_FALSE'
        }
        FUNCTIONS = {
            'length': 'LENGTH_FUNCTION',
            'string': 'STRING_FUNCTION',
            'integer': 'INTEGER_FUNCTION',
            'print': 'PRINT_FUNCTION',
            'sqrt': 'SQUARE_ROOT'
        }
    
    
    
    
    
    # FIX : doesn't work with more than one char.
    for k,v in Lexicon.SYMBOLS.items():
        for char_index in range(len(data) - 1):
            char = data[char_index]
            if char == k:
               for i in range(char_index + 1):
                   lexed.append('')
               lexed[char_index] = (char,v)
    
    
    
    
    #FIX : provides incorrect tag.
    for k,v in Lexicon.KEYWORDS.items():
        for word_index in range(len(datawords) - 1):
            word = datawords[word_index]
            if word == k:
                for i in range(word_index):
                    lexed.append('')
                lexed[word_index] = (word,v)
    
    #FIX : provides incorrect tag.
    for k,v in Lexicon.FUNCTIONS.items():
        for word_index in range(len(datawords) - 1):
            word = datawords[word_index]
            for i in range(word_index):
                lexed.append('')
            lexed[word_index] = (word,v)
    
    
    lexed = [value for value in lexed if value != '']
    # This just removes all empty tokens that were used to bypass index errors, or any useless tokens.
    print(lexed)
    print("Exited lexical analyzer.")
