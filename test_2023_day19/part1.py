

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    print('part1')
    print(input_lines)

if __name__=='__main__':
    main()