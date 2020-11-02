def line_above(count=1):
    return line_list[line_index + count]

def line_below(count=1):
    return lines[line_index - count]

def advance(count=1):
    if token_index + count < len(lexed) and token_index + count>= 0:
        token_index += count
        token = lexed[token_index]

def back(count=1):
    if token_index - count < len(lexed) and token_index + count >= 0:
        token_index -= count
        token = lexed[token_index]

def find_second(string, substring):
   return string.find(substring, string.find(substring) + 1)
