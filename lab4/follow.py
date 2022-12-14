# follow from given grammar

def FOLLOW(grammar, nonterminal):
    follow = set()
    follow_(grammar, nonterminal, follow)
    return follow

def follow_(grammar, nonterminal, follow):
    # if nonterminal is in follow, return
    if nonterminal in follow:
        return
    # add nonterminal to follow
    follow.add(nonterminal)
    # for each production in grammar
    for production in grammar:
        # for each symbol in production
        for i in range(len(production)):
            # if symbol is nonterminal
            if production[i] == nonterminal:
                # if symbol is last symbol in production
                if i == len(production) - 1:
                    # follow_(grammar, production[0], follow)
                    follow_(grammar, production[0], follow)
                # else
                else:
                    # if production[i+1] is terminal
                    if production[i+1] not in grammar:
                        # add production[i+1] to follow
                        follow.add(production[i+1])
                    # else
                    else:
                        # first_(grammar, production[i+1], follow)
                        first_(grammar, production[i+1], follow)
                        # if epsilon is in first
                        if epsilon in first:
                            # follow_(grammar, production[0], follow)
                            follow_(grammar, production[0], follow)


if __name__ == "__main__":
    grammar = {
            "A" : ["cB", "Cc", "daB"],
            "B" : ["bB", "+"],
            "C" : ["aB", "BaB", "+"],
            "D" : ["a", "b"]
        }
    
    from utils import print_grammar
    
    print_grammar(grammar)
    print("FOLLOW(A) = ", FOLLOW(grammar, "A"))
    print("FOLLOW(B) = ", FOLLOW(grammar, "B"))
    print("FOLLOW(C) = ", FOLLOW(grammar, "C"))
    print("FOLLOW(D) = ", FOLLOW(grammar, "D"))