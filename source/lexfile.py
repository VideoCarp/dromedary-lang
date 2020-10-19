# This may later change to a different language.
toparse = """
[]()
""".replace("\n", "")
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


# Functions
def line_above(count=1):
    return line_list[line_list.index(line) + count]

def line_below(count=1):
    return line_list[line_list.index(line) - count]

def space_front(count=1):
    return space_tokenlist[space_tokenlist.index(space_token) + count]

def space_behind(count=1):
    return space_tokenlist[space_tokenlist.index(space_token) - count]

def token_front(count=1):
    return lex_token[lex_token.index(token) + count].replace(" ", "")

def token_behind(count=1):
    return lex_token[lex_token.index(token) - count].replace(" ", "")

def str_token():
    return_value = False
    if token == '"' or token == "'": 
        return True
    else:
        return False


def switch(expression, casevar: dict, returning=False):
    for k,v in cases.items():
        if expression == k:
            if returning == True:
                return v
            else:
                v()


result = []
def newsplitter(arg):
    token_splitters.append(arg)

# Finishing up
for line in line_list:
        for token in lex_token:
            if lex_token.index(token) > len(lex_token):
                if str_token() == False:
                    if token_behind() == "fn":
                        newsplitter(token)
                    elif token_front() == ":=":
                        newsplitter(token)


for token_splitter in token_splitters:
    tok = toparse.replace(token_splitter, "TOKEN_SPLIT")
lex_token = tok.split("TOKEN_SPLIT")
# TODO : Fix issue of 'replace' above doing quite literally
# nothing.
print(tok)
print(lex_token)
