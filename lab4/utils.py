def stringfy(L):
    string = ''
    for l in L:
        string += l + "|"
    return string[:-1]


def print_grammar(grammar):
    for key in sorted(grammar.keys()):
        print(f"{key} ---> {stringfy(grammar[key])}")
    print("\n")