def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

digits = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

digit_dict = {d:i+1 for i, d in enumerate(digits)}

def get_first_num(_line:str):
    line = str(_line)
    while line:
        if line[0].isdigit():
            return int(line[0])
        for digit, value in digit_dict.items():
            if line.startswith(digit):
                return value
        line = line[1:]
    return 0

def get_last_num(_line:str):
    line = str(_line)
    while line:
        if line[-1].isdigit():
            return int(line[-1])
        for digit, value in digit_dict.items():
            if line.endswith(digit):
                return value
        line = line[:-1]
    return 0

def get_sum(line:str):
    return get_first_num(line)*10 + get_last_num(line)

def main():
    lines = get_input_lines()
    total=0
    for line in lines:
        total += get_sum(line)
    print(total)
    
if __name__=='__main__':
    main()