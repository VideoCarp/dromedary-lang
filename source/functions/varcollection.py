control = ["if", "while", "for"]
math = ["+", "-", "*", "%", "/"]
paren = ["(", ")"]
brace = ["{", "}"]
typeid = ["int", "char", "string", "float", "double", "long", "bool", "void", "nil", "static"]
function = ["length", "sqrt", "random"]
comparison = ["==", "!=", ">", "<", ">=", "<="]
keyword = ["return", "switch", "extern", "default", "import", "and", "or", "not", "goto", "register"]

arraytype = []
for each in typeid:
    arraytype.append(f"{each}[]")
    
