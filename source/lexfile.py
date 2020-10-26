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
        SINGLECHAR = {
            '-': 'ARITHMETIC',
            '+': 'ARITHMETIC',
            '*': 'ARITHMETIC',
            '%': 'ARITHMETIC',
            '/': 'ARITHMETIC',
            '(': 'PAREN',
            ')': 'PAREN',
            '[': 'BRACKET',
            ']': 'BRACKET',
            '{': 'BRACE',
            '}': 'BRACE',
            '=': 'EQUAL',
            '==': 'COMPARISON',
            '!=': 'COMPARISON',
            '>': 'COMPARISON',
            '<': 'COMPARISON',
            '>=': 'COMPARISON',
            '<=': 'COMPARISON',
        }
        MULTICHAR = {
            # multichar symbols
            '==': 'COMPARISON',
            '!=': 'COMPARISON',
            '>=': 'COMPARISON',
            '<=': 'COMPARISON'
            # keywords
            'if': 'CONTROL',
            'while': 'CONTROL',
            'for': 'CONTROL',
            'true': 'BOOLEAN',
            'false': 'BOOLEAN',
            'int': 'STATIC',
            'string': 'STATIC',
            'char': 'STATIC',
            'float': 'STATIC',
            # functions
            'length': 'BUILT_IN_FUNCTION',
            'string': 'BUILT_IN_FUNCTION',
            'integer': 'BUILT_IN_FUNCTION',
            'print': 'BUILT_IN_FUNCTION',
            'println': 'BUILT_IN_FUNCTION'
        }
       

    
    
    
    
    
    # FIX : doesn't work with more than one char.
    for k,v in Lexicon.SINGLECHAR.items():
        for char_index in range(len(data) - 1):
            char = data[char_index]
            nextchar = data[char_index + 1]
            if char == k and nextchar != '=':
               for i in range(char_index + 1):
                   lexed.append('')
               lexed[char_index] = (char,v)
    
    
    
    for k,v in Lexicon.MULTICHAR.items():
        for word_index in range(len(datawords) - 1):
            word = datawords[word_index]
            if word == k and datawords[word_index + 1] != '(':
                for i in range(word_index + 1):
                    lexed.append('')
                lexed[char_index] = (char,v)
    
    lexed = [value for value in lexed if value != '']
    # This just removes all empty tokens that were used to bypass index errors, or any useless tokens.
    print(lexed)
    print("Exited lexical analyzer.")
