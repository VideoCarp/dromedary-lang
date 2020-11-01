import lexfile as lexer
from functions import color_collection as colors


def send(args,clr=colors.default):
    print(f"{clr}{args}{colors.end}")

#send("message", Colors.color")

colors.send("Dromedary Language Compiler", colors.bold)

print(f"Type a {colors.warning}{colors.bold}path{colors.end} to a script to compile it.
      : ",end='')
file = input()


# send 'data' variable
with open(file, "r") as f:
      colors.send("Sending data to lexical analyzer...", colors.green)
      lexer.analyze(f.read())

