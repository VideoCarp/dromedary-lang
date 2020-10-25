class colors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underlined = '\033[4m'

#print(f"{colors.COLOR}Hi{colors.ENDC}")

def err_send(color=error,args):
    print(f"{colors.color}{args}{colors.end})
