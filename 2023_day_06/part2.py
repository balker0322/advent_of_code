

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    tr = ''.join(input_lines[0].split(':')[-1].split())
    dr = ''.join(input_lines[1].split(':')[-1].split())

    t = int(tr)
    d = int(dr)
    total = 0

    for ti in range(t+1):
        if ti*(t-ti) > d:
            total += 1
            
    print(total)



if __name__=='__main__':
    main()