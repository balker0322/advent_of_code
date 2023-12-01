def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_first_num(_line:str):
    line = str(_line)
    while line:
        if line[0] in '0123456789':
            return int(line[0])
        line = line[1:]
    return 0

def get_last_num(_line:str):
    line = str(_line)
    while line:
        if line[-1] in '0123456789':
            return int(line[-1])
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