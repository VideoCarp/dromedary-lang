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

def newsplitter(arg):
    token_splitters.append(arg)
