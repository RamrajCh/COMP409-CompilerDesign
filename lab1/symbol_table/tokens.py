from valid_tokens import ( KEYWORDS, WHITESPACE, SEPARATOR, OPERATORS)
from utils import (list_to_str, valid_identifier, valid_float, 
                    valid_integer, valid_string, is_delimiter)
tokens = []

def search_token(S:str):
    return S in tokens

def detect_token(buffer:list):
    lexeme_begin = 0
    forward = 0
    N = len(buffer)

    while forward < N and lexeme_begin <= forward:
        input = buffer[forward]
        if not is_delimiter(input):
            forward += 1
        
        if is_delimiter(input) and lexeme_begin == forward:
            token = input
            if not search_token(token):
                tokens.append(token)
            forward += 1
            lexeme_begin = forward

        elif (is_delimiter(input) and lexeme_begin != forward) or\
                (forward == N and forward != lexeme_begin):
            token = list_to_str(buffer[lexeme_begin:forward])
            if not search_token(token):
                tokens.append(token)
            lexeme_begin = forward
    classify_token()

def classify_token():
    for token in tokens:
        if token in KEYWORDS: print(f"{token} -> keyword")
        
        elif valid_integer(token): print(f"{token} -> integer literal")
        
        elif valid_float(token): print(f"{token} -> float literal")
        
        elif valid_string(token): print(f"{token} -> string literal")
        
        elif valid_identifier(token): print(f"{token} -> identifier")
        
        elif token in OPERATORS: print(f"{token} -> operator")
        
        elif token in WHITESPACE: print(f"'{token}' -> whitespace")
        
        elif token in SEPARATOR: print(f"{token} -> separator")