import sys

if __name__ == "__main__":
    example = sys.argv[1]
    f = open(f"cfg{example}.txt", "r")
    unclean_cfg = f.readlines()
    f.close()
    unclean_cfg = [c.strip() for c in unclean_cfg]
    grammar = {}
    for rule in unclean_cfg:
        rule_ = rule.split("--->")
        grammar[rule_[0].strip()] = rule_[1].strip().split("|")
        
    from left_resursion import remove_left_recursion, print_grammar
    
    print("Grammar having left Recursion:\n")
    print_grammar(grammar)
    remove_left_recursion(grammar)
    print("Grammar after removing left Recursion:\n")
    print_grammar(grammar)