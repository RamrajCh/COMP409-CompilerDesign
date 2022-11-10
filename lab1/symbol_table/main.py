from tokens import detect_token
from utils import clean_buffer

if __name__ == "__main__":
    print("\n")
    with open("./lab1/symbol_table/input.txt", 'r') as input:
        unclean = input.readlines()
        buffer = clean_buffer(unclean)
        detect_token(buffer)
    print("\n")