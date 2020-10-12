# This may later be written in a different language.
from lexfile import *

class DeclaringErrror(Exception):
    pass
def currentline():
    return line_list[line_list.index(line)]

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
            
