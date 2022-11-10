class State(object):
    def __init__(self, key:str) -> None:
        self.start = True if "-->" in key else False
        self.final = True if "*" in key else False
        self.key = key.replace('-->', '').replace("*", "")

    def __repr__(self) -> str:
        repr = ''
        if self.start:
            repr += '-->'
        if self.final:
            repr += '*'
        return repr + "q"+ self.key


class DFA(object):
    def __init__(self, start_state:State, alphabets:list) -> None:
        self.start_state = start_state
        self.alphabets = alphabets
        self.transition_table = {
            self.start_state: {alphabet:"" for alphabet in self.alphabets},
        }
    
    def add_state(self, state:State) -> None:
        self.transition_table[state] = {alphabet:"" for alphabet in self.alphabets}
    
    def add_transition(self, tail_state:State, head_state:State, alphabet:str):
        self.transition_table[tail_state][alphabet] = head_state
    
    def validate_input(self, input):
        state = self.start_state
        for character in input:
            if not character in self.alphabets:
                return False
            state = self.transition_table[state][character]
        return True if state.final else False
    
    def __repr__(self) -> str:
        repr = 'state\t|\t'
        for alphabet in self.alphabets:
            repr += f"{alphabet}\t|\t"
        repr += '\n'
        for key, values in self.transition_table.items():
            repr += f"{key}\t|\t"
            for value in values.values():
                repr += f"q{value.key}\t|\t"
            repr += '\n'
        repr += '\n'
        return repr


if __name__ == "__main__":
    q0 = State('-->0')
    # print(q0.start, q0.final)
    q1 = State('1')
    q2 = State('*2')
    q3 = State('*3')

    dfa = DFA(q0,['0', '1'])
    dfa.add_state(q1)
    dfa.add_state(q2)
    dfa.add_state(q3)

    dfa.add_transition(q0, q1, '0')
    dfa.add_transition(q0, q0, '1')
    dfa.add_transition(q1, q2, '0')
    dfa.add_transition(q1, q3, '1')
    dfa.add_transition(q2, q2, '0')
    dfa.add_transition(q2, q3, '1')
    dfa.add_transition(q3, q1, '0')
    dfa.add_transition(q3, q0, '1')

    print(dfa)

    print(dfa.validate_input('0'))