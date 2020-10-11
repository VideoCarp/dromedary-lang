# This may later change to a different language.
toparse = ""
line_list = toparse.split("\n")
space_tokenlist = toparse.split(" ")

token_splitters = []

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
    "false", "true", "null", "pass", "fn"
]

for ks in keyword_splitters:
    token_splitters.append(ks)
for ss in symbol_splitters:
    token_splitters.append(ss)


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

def str_token():
    return_value = False
    if token == '"' or token == "'": return_value = True
result = []
for line in line_list:
    for space_token in space_tokenlist:
        for token in lex_token:
            if str_token() == False:
                if token == ":=": token_splitters.append(token_behind().replace(" ", ""))
                if token == "func": token_splitters.append(token_front().replace(" ", ""))

print("\n".join(result))
