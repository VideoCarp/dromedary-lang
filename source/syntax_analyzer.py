def run(lexed: list, lines: list) -> str:
    print("Entered syntax analyzer.")
    for token_index in range(len(lexed) - 1):
        for line_index in range(len(lines) - 1):
            token: str = lexed[token_index]
            line: str = lines[line_index]
            pass
