import re
import json
def analyze(toparse=None):
    if toparse is None or toparse.replace(" ", "") == "":
       raise Exception("Lexer did not get enough info.")
    print("Successfully entered lexical analyzer.")
    toparse = toparse.replace("	", "  ") # tab
    GSUB = {}
    with open("config.json") as f:
        GSUB = json.loads(f.read())

    for k,v in GSUB.items():
        toparse.replace(k,v)


    data = toparse
    lexed = []
    lexdata = []
    lines = data.split("\n")
    class Lexicon:
        ARITHMETICS = ["-", "+", "*", "%", "/"]
        RIGHTLEFT = ["(", ")", "[", "]", "{", "}", r" "]
        COMPARISONS = [">", "<"]

    full = []
    full = Lexicon.ARITHMETICS + Lexicon.RIGHTLEFT + Lexicon.COMPARISONS
    ending = ""
    for each in full:
       nospace = "\\".join(full)
    
    lexed = re.split(fr"([{nospace}])", data)
    for valueindex in range(len(lexed) - 1):
        lexed[valueindex] = lexed[valueindex].replace("\n", "").replace("  ", "")
    lexed = [value for value in lexed if value != '' and value != ' ']
    print(lexed)
    print("Exited lexical analyzer.")
