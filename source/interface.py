class Colors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underlined = '\033[4m'
    gray = '\u001b[30;1m'
    default = ''


def send(args,clr=Colors.default):
    print(f"{clr}{args}{colors.end}")

#send("message", Colors.color")

send("Dromedary Language Compiler", Colors.bold)

print(f"Type a {Colors.warning}path{colors.end} to a script to compile it.",end='')
file = input()


with open(file, "r") as f:
    print("Entering lexical analysis.")
    import lexfile
    lexfile.data = f.read()
