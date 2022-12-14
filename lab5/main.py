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
        
    from left_factor import remove_left_factors, print_grammar
    
    print("Grammar having left Factors:\n")
    print_grammar(grammar)
    remove_left_factors(grammar)
    print("Grammar after removing left Factors:\n")
    print_grammar(grammar)