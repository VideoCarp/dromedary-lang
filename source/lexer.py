# This may later change to a different language.
toparse = ""
line_list = toparse.split("\n")
space_tokenlist = toparse.split(" ")
lex_token = []

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
        if 
