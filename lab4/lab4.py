def get_first(a, first, c):
    if first.get(a):
        return first[a]
    elif a in terminal:
        return {a}
    else:
        first[a] = set([])
        for element in c:
            if element[0] == a:
                for each in (element[1:]):
                    value = 0
                    while ('ε' in get_first(each.split()[value], first, c) 
                            and len(each.split()[value+1:]) > 0):
                        first[a]\
                        .update(get_first(each.split()[value], first, c) - {'ε'})
                        value = value +1 
                    first[a].update(get_first(each.split()[value], first, c))
        return first[a]

def get_follow( follow, c):
    for element in c:
        for each in element[1:]:
            j = each.split()
            for i in range(len(j)):
                
                if j[i] in non_terminal:
                    if not follow.get(j[i]):
                        follow[j[i]]= set([])
                    if i < len(j)-1:
                        if j[i+1] in non_terminal:
                            value = i+1
                            while ('ε' in first[j[value]] and len(j[value+1:]) >= 1):
                                follow[j[i]].update(first[j[value]] - {'ε'})
                                value = value+1
                            follow[j[i]].update(first[j[value]] - {'ε'})
                            if len(j[value+1:]) <= 0:
                                follow[j[i]].update(follow[element[0]])
                        else:
                            follow[j[i]].update({j[i+1]})
                    else:               
                        follow[j[i]].update(follow[element[0]])
                        
def stringify(set):
    # {'id', '('}
    string = '{'
    for s in set:
        string += f"{s}, "
    string = string[:-2]
    return string + '}'

if __name__ == "__main__":
    import re
    import sys
    example = sys.argv[1]
    f = open(f"cfg{example}.txt", "r")
    unclean_cfg = f.readlines()
    f.close()
    grammar = ''
    for l in unclean_cfg:
        grammar += l
    
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
        print(f'First({key}) = {stringify(first[key])}')
    print('\n')
    
    print(f'The follow of the grammar is:')
    pfollow = ''
    for key in follow:
        print(f'Follow({key}) = {stringify(follow[key])}')
    print("\n")
