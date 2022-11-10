from regex import check_valid

if __name__ == "__main__":
    inputs = input("Give input for regex ab(a+b)*ba separated by commas:\n")
    inputs = inputs.split(',')

    for input in inputs:
        input = input.strip()
        print(f"{input} -> {check_valid(input)}")
    
    print("\n")
