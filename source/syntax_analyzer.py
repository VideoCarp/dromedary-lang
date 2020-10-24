#Unused rn
from lexfile import *
from functions import *
analyzed = []
numlist = [1,2,3,4,5,6,7,8,9,0]


# all iterations we'd ever need. 
for line in line_list:
    for token in lex_token:
        for kw in keyword_splitters:
        # Error handling
            if token == "=" and token_behind() not in token_splitters:
                print(f"DeclaringError: Attempt to modify variable '{token_behind()}' at line {currentline()}\
                before assignment. Define the variable with ':=', '=' is reserved for reassigning a value.")

            if token == "fn" and token_front() == kw or token == ":=" and token_front() == kw:
                 print(f"DeclaringError: Attempt to declare function or variable with name of a reserved keyword, '{kw}'\
                 at '{token}{token_front()}' in line {currentline()}.\
                 Consider renaming the variable or function to an unreserved keyword.")

                    


            # Analyze
            token_analysis = {} # empty rn, this switch cases for 'token' var.
            switch(token, token_analysis)
            type_analyze()
            global_replacements = {
                "'": '"',
                "print(": "printf",
            } # currently not worth iterating, but it will grow.
            for k,v in global_replacements.items():
                line.replace(k,v)

            # This makes it so '(' and ')' aren't required.
            if "if " in line and "{" in line:
                analyzed.append(line.replace("if ", "if (").replace("{", ") {"))

                    
                
                
