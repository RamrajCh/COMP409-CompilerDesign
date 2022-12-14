"""
grammar = {
            "A" : ["AcB", "cC", "c"],
            "B" : ["bB", "id"],
            "C" : ["CaB", "BaB", "B"],
        }
        
"""
def first_(grammar):
    FIRST = {key:[] for key in grammar.keys()}
    for N in grammar.keys():
        F = first(grammar, N)
        FIRST[N] += F
    return {key:set(values) for key, values in FIRST.items()}

def first(grammar, N):
    F = []
    for R in grammar[N]:
        if R[0] not in grammar.keys():
            F += R[0]
        else:
            F += first(grammar, R[0])
    return F

if __name__ == "__main__":
    grammar = {
            "A" : ["cB", "Cc", "daB"],
            "B" : ["bB", "+"],
            "C" : ["aB", "BaB", "+"],
            "D" : ["a", "b"]
        }
    
    from utils import print_grammar
    
    print_grammar(grammar)
    print(first_(grammar))