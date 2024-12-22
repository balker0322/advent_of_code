import re

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    total = 0
    for line in input_lines:
        results = re.findall("mul\(\d+\,\d+\)", line)
        for r in results:
            rr = re.findall('\d+', r)
            total += int(rr[0])*int(rr[1])
    print(total)

if __name__=='__main__':
    main()