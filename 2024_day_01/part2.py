

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    l1, l2 = [], []
    for line in input_lines:
        num1, num2 = line.split()
        l1.append(int(num1))
        l2.append(int(num2))

    total = 0
    for n in l1:
        c = len([i for i in l2 if i==n])
        total += n*c

    print(total)

if __name__=='__main__':
    main()