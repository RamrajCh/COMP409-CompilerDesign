# Write a program to remove the left recursion from the given grammar.
import copy

def has_left_recursion(grammar):
    """Check if the grammar has any left recursion

    Args:
        grammar (dict): A dictionary with non terminal symbol as key and list of production rules as values.
        Example:
        grammar = {
            "A" : ["AcB", "cC", "c"],
            "B" : ["bB", "id"],
            "C" : ["CaB", "BaB", "B"],
        }

    Returns:
        bool: Returns False if there are not any left recursion.
        tuple: Returns (key, recursion) that have left recursion
    """
    for V, R in grammar.items():
        recursion = list(map(lambda x:x[0]==V,R))
        if any(recursion):
            return V
    return False

def remove_left_recursion(grammar):
    """Removes left ecursion, if any, of the passed grammar.

    Args:
        grammar (dict): A dictionary with non terminal symbol as key and list of production rules as values.
        Example:
        grammar = {
            "A" : ["AcB", "cC", "c"],
            "B" : ["bB", "id"],
            "C" : ["CaB", "BaB", "B"],
        }
    """
    while has_left_recursion(grammar):
        V = has_left_recursion(grammar)
        rule = copy.copy(grammar[V])
        rule_ = []
        for R in grammar[V]:
            if V == R[0]: 
                rule.remove(R)
                rule_.append(R[1:]+V)
            else: 
                rule.remove(R)
                rule.append(R+V+"'")
        grammar[V] = rule
        grammar[V+"'"] = rule_ + ['epsilon']
    for N, R in grammar.items():
        if not R: R.append(N+"'")
    
def stringfy(L):
    """Stringyfy the production rule

    Args:
        L (list): A list containing the RHS of production rules.
        Example
        L = ["AcB", "cC", "c"]

    Returns:
        str: A string of the given list concatenated together with | in the middle.
    """
    string = ''
    for l in L:
        string += l + "|"
    return string[:-1]


def print_grammar(grammar):
    """Prints the grammar.

    Args:
        grammar (dict): A dictionary with non terminal symbol as key and list of production rules as values.
        Example:
        grammar = {
            "A" : ["AcB", "cC", "c"],
            "B" : ["bB", "id"],
            "C" : ["CaB", "BaB", "B"],
        }
    """
    for key in sorted(grammar.keys()):
        print(f"{key} ---> {stringfy(grammar[key])}")
    print("\n")

if __name__ == "__main__":
    # grammar = {
    #     "A" : ["AcB", "cC", "c"],
    #     "B" : ["bB", "id"],
    #     "C" : ["CaB", "BaB", "B"],
    # }
    grammar = {
        "A" : ["aB", "aC", "Ad", "Ae"],
        "B" : ["bBc", "f"],
        "C" : ["g"]
    }
    print_grammar(grammar)
    remove_left_recursion(grammar)
    print_grammar(grammar) 