import sys
import re
from lab4_joshi import get_first, get_follow

if __name__ == "__main__":
    example = sys.argv[1]
    f = open(f"cfg{example}.txt", "r")
    unclean_cfg = f.readlines()
    f.close()
    grammar = ''
    for l in unclean_cfg:
        grammar += l
    print(grammar)
    
    grammar = grammar.strip()
    a = re.split("\n", grammar)
    b = []
    c = []
    every_variable = []
    non_terminal = []

    for element in a:
        b.append(re.split(r"->|\|", element))
        
    for element in b:
        d = []
        for side in element:
            stripped_str = side.strip()
            d.append(stripped_str)
        c.append(d)

    for element in c:
        joined = (' | '.join(str(a) for a in element[1:]))
        non_terminal.append(*element[0].split())
        for each in element:
            every_variable.extend(each.split())
        
        
    terminal = set(every_variable) - set(non_terminal)

    print(f'The given grammar is:\n{grammar}\n')
            
    first = {}
    follow = {f"{non_terminal[0]}" : {'$'}}

    for each_non_terminal in non_terminal:
        get_first(each_non_terminal, first, c)

    get_follow(follow,c)
    
    print(f'The first of the grammar is:')
    for key in first:
        print(f'First({key}) = {first[key]}')
    print("\n")
    
    print(f'The follow of the grammar is:')
    for key in follow:
        print(f'Follow({key}) = {follow[key]}')
    print("\n")