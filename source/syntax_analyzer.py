from functions import *
from functions import varcollection as cat # category
def run(lexed: list, lines: list) -> str:
    print("Entered syntax analyzer.")
    for token_index in range(len(lexed) - 1):
        for line_index in range(len(lines) - 1):
            token: str = lexed[token_index]
            line: str = lines[line_index]
                if "#interop" not in line:
                    if line.find("#") >= 0:
                        line = line[:line.find("#")]
                    if line.replace(" ", "").endswith("{") == False and line.replace(" ", "").endswith("}") == False:
                        lines[line_index] = f"{line};"
