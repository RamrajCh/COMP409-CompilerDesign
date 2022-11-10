from valid_tokens import DELIMITER

def list_to_str(L):
    S = ''
    for s in L:
        S += s
    return S

def valid_integer(S:str):
    return S.isdigit()

def valid_float(S:str):
    try:
        float(S)
    except ValueError:
        return False
    return True

def valid_string(S:str):
    return S[0] == "'" and S[-1] == "'" and len(S) > 1

def valid_identifier(S:str):
    valid = False
    if S[0].isalpha() or S[0]=="_":
        for s in S:
            if s.isalnum() or s=="_":
                valid = True
            else:
                valid = False
                break
    return valid

def clean_buffer(unclean):
    # remove whitespaces
    unclean = [u.strip() for u in unclean]
    # create list
    buffer = []
    for line in unclean:
        for l in line:
            buffer.append(l)
    return buffer

def is_delimiter(S:str):
    return S in DELIMITER