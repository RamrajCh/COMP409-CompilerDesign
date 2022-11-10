# Language that contains alphabets {a, b} which starts with ab and ends with ba

REGEX = "ab(a+b)*ba"


def check_valid(input):
    if len(input) < 4:
        return 'invalid'

    if not input[0:2] == REGEX[0:2]:
        return 'invalid'

    if not input[-1:-3:-1] == REGEX[-1:-3:-1]:
        return 'invalid'

    if not set(list(input)) == {'a', 'b'}:
        return 'invalid'

    return 'valid'


