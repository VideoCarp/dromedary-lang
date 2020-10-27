from functions import color_collection
from functions import lexer_functions

#print(f"{colors.color}Hi{colors.end}")
KEY_WORDS = [
    "break", 
    "case", 
    "char", 
    "continue", 
    "do", 
    "default", 
    "double", 
    "else", 
    "enum", 
    "extern", 
    "for", 
    "if", 
    "goto", 
    "float", 
    "int", 
    "long", 
    "register", 
    "return", 
    "static", 
    "switch", 
    "void", 
    "while",
    ">",
    ">=",
    "<=",
    "!=",
    "==",
    "and",
    "or",
    "not",
    "{",
    "}",
    "(",
    ")",
    "println",
    "import",
    "print",
    ".",
]
def any_in(args, inornot=True, c=1):
    if inornot == True:
        for each in args:
            if each in line:
                return True
    elif inornot == False:
        for each in args:
            if each != token_behind(c):
                return True

typelist = ["int", "string", "char", "double", "float", "long"]
#send("message", colors.color")

identifiers = {}
for item in KEY_WORDS:
    identifiers[item] = "keyword"

errors = []
def send_error(text, clr=colors.error):
    errors.append(f"""at {line}
    {colors.bold}dromedary, line {line_index}:{colors.end}{clr}{text}
    """)
result = []
def handle(lexdata, linelist):
    lexed = lexdata
    lines = linelist
    for token_index in range(len(lexed) - 1):
        for line_index in range(len(lines) - 1):
            token = lexed[token_index]
            line = lines[line_index]
            
            if token_index + 2 < len(lexed):
                print("Entering error handling...")
                if "#interop" not in line:
                    if token == "=" and any_in(typelist):
                        identifiers[token_front()] = token_behind(2)
                    elif token == "=" and not any_in(typelist) and token_behind() not in typelist:
                        send_error(f"attempt to reassign undefined '{token_behind()}'")
                    if token == "(" and any_in(typelist, False, 2):
                        identifiers[token_behind(1)] = token_behind(2)
                    if token == "(" and token_behind() not in identifiers:
                        send_error(f"undefined function '{token_behind()}'")
                    if token not in identifiers:
                        send_error(f"cannot understand token '{token}'. possibly undefined")
                else:
                    result.append(line)

class compiler(Exception):
    pass
if errors != []:
    for error in errors:
        print(f"{colors.bold}{'_' * 15}")
        print(error)
    raise compiler("errors encountered.")
