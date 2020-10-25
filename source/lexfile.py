
data = r"""

"""
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
    for char in data:
        if char == k:
           location = data.index(char)
           for i in range(location + 1):
               lexed.append('')
           lexed[location] = (char,v)




#FIX : only finds one word.
for k,v in Lexicon.KEYWORDS.items():
    for word in datawords:
        if word == k:
            location = datawords.index(word)
            for i in range(location):
                lexed.append('')
            lexed[location] = (word,k)

#FIX : only finds one word
for k,v in Lexicon.FUNCTIONS.items():
    for word in datawords:
        if word == k:
            location = datawords.index(word)
            for i in range(location):
                lexed.append('')
            lexed[location] = (word,k)


print(lexed)
