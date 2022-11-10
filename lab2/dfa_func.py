def dfa(states, inputs):
    tran_table = [[None for i in range(inputs+1)] for j in range(states)]
    for i in range(states):
        for j in range(inputs):
            tran_table[i][j] = input('State {} is transitioned by input {} to state:\t\t'.format(i,j))
        feri = True
        while(feri):
            is_final = str(input('Is state {} final state? (Y/y) or (N/n):\t\t\t'.format(i)))
            if is_final == 'Y' or is_final == 'y':
                tran_table[i][inputs] = True
                feri = False
            elif  is_final == 'N' or is_final=='n':
                tran_table[i][inputs] = False
                feri = False
            else:
                print('Enter a valid input')
                feri= True
    
    check = [x for x in input('Strings you want to check, seperated by whitespaces:\t').split()]
    for word in check:
        checker(word, tran_table)

def checker(word, tran_table):
    final_state = 0
    for character in word:
            if not character.isdigit():
                print('You entered invalid character')
                return
            elif int(character) not in range(inputs):
                print('You entered invalid charactera')
                return
            else:
                final_state = int(tran_table[final_state][int(character)])
    if tran_table[final_state][2]:
        print('Valid String')
    else:
        print('Invalid String')

if __name__ == '__main__':
    states = int(input('Enter the number of states:\t\t\t\t'))
    inputs = int(input('Enter the number of valid input characters:\t\t'))
    dfa(states, inputs)
