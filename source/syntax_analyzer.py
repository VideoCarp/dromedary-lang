# This may later be written in a different language.
from lexfile import *

analyzed = []
class DeclaringErrror(Exception):
    pass
def currentline():
    return line_list[line_list.index(line)]

def modify_token(tok=token, old, new):
    analyzed = analyzed.append(tok.replace(old, new))

def mod_replace(t=token, oldvalue, newvalue, extra=False):
    if t == token: 
        t = token == oldvalue
    
    if t:
        if extra != false:
           extra()
        modify_token(oldvalue, newvalue)

def linemod(old, new):
    analyzed = analyzed.append(line.replace(old, new))

for line in line_list:
    for token in lex_token:
        for kw in keyword_splitters:
        # Error handling
            if token == "=" and token_behind() not in token_splitters:
                raise DeclaringError(f"Attempt to modify variable '{token_behind()}' at line {currentline()}\
                before assignment. Define the variable with ':=', '=' is reserved for reassigning a value.")
            if token == "fn" and token_front() == kw or token == ":=" and token_front() == kw:
                raise DeclaringError(f"Attempt to declare function or variable with name of a reserved keyword, '{kw}'\
                 at '{token}{token_front()}' in line {currentline()}.\
                 Consider renaming the variable or function to an unreserved keyword.")

            # Analyze
            if ":=" in line:
                mod_replace(token == ":=" and token_behind() not in token_splitters, ":=", "=")
            if "fn" in line:
                mod_replace(token == "fn" and token_front() not in token_splitters, "fn", "def")
            if "iterate" in line:
                analyzed = analyzed.append(line.replace("
