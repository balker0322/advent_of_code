

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    tr = [int(x) for x in input_lines[0].split(':')[-1].split()]
    dr = [int(x) for x in input_lines[1].split(':')[-1].split()]

    prod = 1
    for t, d in zip(tr, dr):
        total = 0
        for ti in range(t+1):
            if ti*(t-ti) > d:
                total += 1
        prod *= total

    print(prod)



if __name__=='__main__':
    main()