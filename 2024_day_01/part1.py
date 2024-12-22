

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    l1, l2 = [], []
    for line in input_lines:
        num1, num2 = line.split()
        l1.append(int(num1))
        l2.append(int(num2))

    l1.sort()
    l2.sort()

    total = 0
    for n1, n2 in zip(l1, l2):
        total += abs(n2 - n1)

    print(total)

if __name__=='__main__':
    main()