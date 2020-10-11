# This may later change to a different language.
toparse = ""
line_list = toparse.split("\n")
space_tokenlist = toparse.split(" ")

# Unclear, or not fully/easily visible will be commented.
symbol_splitters = [
    ":=", "+", "-", "*", "%", "/", "**", 
    "(", ")", "\"", "'", "[", "]" # Parantheses, quotes, and []
    "==", "!=", ">=", "<=", ">", "<",
    ":", "1", "2", "3", "4", "5", "6", "7", "8"
]

keyword_splitters = [
    "if", "while", "for", "elif", "else",
    "and", "or", "not", "is", "is not",
]
token_splitters = []


for token_splitter in token_splitters:
    tok = toparse.replace(token_splitter, "TOKEN_SPLIT")
lex_token = tok.split("TOKEN_SPLIT")

def line_above(count=1):
    return line_list[line_list.index(line) + count]

def line_below(count=1):
    return line_list[line_list.index(line) - count]

def space_front(count=1):
    return space_tokenlist[space_tokenlist.index(space_token) + count]

def space_behind(count=1):
    return space_tokenlist[space_tokenlist.index(space_token) - count]

def token_front(count=1):
    return lex_token[lex_token.index(token) + count]

def token_behind(count=1):
    return lex_token[lex_token.index(token) - count]

for line in line_list:
    for space_token in space_tokenlist:
        if ":=" in line:
            token_splitters.append(str(space_behind()))
