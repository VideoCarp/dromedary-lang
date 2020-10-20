def currentline():
    return line_list[line_list.index(line)]

def modify_token(tok=token, old, new):
    analyzed = analyzed.append(tok.replace(old, new))

def mod_replace(t=token, oldvalue, newvalue, extra=False):
    if t == token: 
        t = token == oldvalue
    
    if t:
        if extra != false:
           extra()
        modify_token(oldvalue, newvalue)

def linemod(old, new):
    analyzed = analyzed.append(line.replace(old, new))

def type_analyze():
    if ":=" in line:
        for numvalue in numlist:
            tkswitch = {
                        token_front().startswith('"') or token_behind.startswith("'"):\
                        lambda: analyzed.append(line.replace(line, f'char[] {line}').replace(":=", "="))
                        lambda: token_front().startswith(num): analyzed.append(line.replace(line, f'int {line}').replace(":=", "="))
                       }
                    for k,v in tkswitch.items():
                        if k:
                            v()
