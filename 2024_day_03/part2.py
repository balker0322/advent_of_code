import re

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    total_results = []
    for line in input_lines:
        results = re.findall(r"(mul\(\d+\,\d+\))|(do\(\))|(don\'t\(\))", line)
        results = [x+y+z for x, y, z in results]
        total_results += results

    total = 0
    enable_mul = True
    for r in total_results:
        if r==r"do()":
            enable_mul = True
            continue
        if r==r"don't()":
            enable_mul = False
            continue
        if enable_mul==False:
            continue
        rr = re.findall('\d+', r)
        total += int(rr[0])*int(rr[1])
    print(total)

if __name__=='__main__':
    main()