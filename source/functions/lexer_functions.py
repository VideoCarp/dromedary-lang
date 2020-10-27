def line_above(count=1):
    return line_list[line_list.index(line) + count]

def line_below(count=1):
    return line_list[line_list.index(line) - count]


def token_front(count=1):
    return lexed[token_index + count]

def token_behind(count=1):
    return lexed[token_index - count]


def switch(expression, casevar: dict, returning=False):
    for k,v in cases.items():
        if expression == k:
            if returning == True:
                return v
            else:
                v()

def newsplitter(arg):
    token_splitters.append(arg)

def find_second(string, substring):
   return string.find(substring, string.find(substring) + 1)
