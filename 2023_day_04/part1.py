
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()

    total = 0
    for line in input_lines:
        wl, ah = line.split(':')[-1].split('|')
        wl = wl.split()
        ah = ah.split()
        point = 0
        for a in ah:
            if a in wl:
                if point == 0:
                    point = 1
                    continue
                point *= 2
        total+=point

    print(total)


if __name__=='__main__':
    main()