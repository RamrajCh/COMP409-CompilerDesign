# Write a program to demonstrate left factoring from a left factored grammar.
"""
{
    "A" : ["bcB", "bcC", "c"],
    "B" : ["bB", "bC"],
    "C" : ["aB", "BaB", "B"],
}
"""
import copy
def substring(str1, str2):
    substring = ''
    i = 0
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        substring += str1[i]
        i+=1
    return substring

def has_left_factor(grammar):
    for lhs, rhs in grammar.items():
        for i in range(len(rhs)):
            for j in range(i+1, len(rhs)):
                s = substring(rhs[i], rhs[j])
                if s:
                      return lhs, s       

def remove_left_factors(grammar):
    while has_left_factor(grammar):
        key, s = has_left_factor(grammar)
        rule = copy.copy(grammar[key])
        rule_ = []
        for r in grammar[key]:
            if r.startswith(s):
                rule.remove(r)
                t = r.replace(s, '') if not r==s else 'epsilon'
                rule_.append(t)
        rule.append(s + f"{key}'")
        grammar[key] = rule
        grammar[f"{key}'"] = rule_

def stringfy(L):
    string = ''
    for l in L:
        string += l + "|"
    return string[:-1]


def print_grammar(grammar):
    for key in sorted(grammar.keys()):
        print(f"{key} ---> {stringfy(grammar[key])}")
    print("\n")
        
if __name__ == "__main__":
    grammar = {
        "A" : ["bcB", "bcC", "c"],
        "B" : ["bB", "bC"],
        "C" : ["aB", "BaC", "B"],
    }
    print_grammar(grammar)
    remove_left_factors(grammar)
    print_grammar(grammar)