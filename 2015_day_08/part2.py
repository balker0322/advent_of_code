import re


def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    
    total = 0

    for line in input_lines:
        total -= len(line)
        line = line.lower()
        line_char_count = 0
        if r:=re.findall(r'\\x', line):
            line = line.replace('\\x', '\\')
            line_char_count += len(r)
        for c in line:
            if c in '1234567890abcdefghijklmnopqrstuvwxyz':
                line_char_count += 1
                continue
            line_char_count += 2
        total = total + 2 + line_char_count
    
    print(total)

if __name__=='__main__':
    main()