# This may later change to a different language.
from functions import *
toparse = """
[]()
"""
line_list = toparse.split("\n")
space_tokenlist = toparse.split(" ")

token_splitters = ["\n"]

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

result = []

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
