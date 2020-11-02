from functions import *
from functions import varcollection as cat # category

def run(lexed: list, lines: list) -> str:
    print("Entered syntax analyzer.")
    resulting: list = []
    for token_index in range(len(lexed) - 1):
        for line_index in range(len(lines) - 1):
            token: str = lexed[token_index]
            line: str = lines[line_index]
                if "#interop" not in line:
                    resin: str = line # result_instance
                    if line.find("#") >= 0:
                        resin = resin[:resin.find("#")]

                    if line.replace(" ", "").endswith("{") == False and line.replace(" ", "").endswith("}") == False \
                    and line.replace(" ", "").endswith(";") == False:
                        resin = f"{resin};"
                        
                    if token == "string":
                        advance()
                        # string hello = "Hello World!"
                        # char hello[] = "Hello World!";
                        resin = resin.r(resin, f"char {token}[] =")
                        
                        
                 elif "#interop" in line:
                        resulting.append(resin)

                    
