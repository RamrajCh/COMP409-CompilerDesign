import sys
from dfa import State, DFA

if __name__ == "__main__":
    example = sys.argv[1]
    with open(f'table{example}.txt', 'r') as file:
        unclean = file.readlines()
        unclean = [u.strip() for u in unclean]
    print(f"\n{unclean.pop(0)}\n")
    alphabets = unclean.pop(0).split("|")
    unclean = [u.split("|") for u in unclean]
    states = [State(u.pop(0)) for u in unclean]
    dfa = DFA(states[0], alphabets)
    for state in states:
        dfa.add_state(state)
    for i in range(len(states)):
        for j in range(len(alphabets)):
            dfa.add_transition(states[i], 
                        states[int(unclean[i][j])], 
                        alphabets[j])
    print("The transition table for DFA is:\n")
    print(dfa)
    inputs = input("Give some strings to validate: \n")
    inputs = inputs.split(',')
    inputs = [input.strip() for input in inputs]
    for input in inputs:
        if dfa.validate_input(input):
            print(f"{input} -> valid")
        else:
            print(f"{input} -> invalid")