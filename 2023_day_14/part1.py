
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def print_rock(rocks):
    print()
    for row in rocks:
        print(''.join(row))

def shift_rocks(rocks):
    rocks = list(rocks)
    swap = True
    while swap:
        swap=False
        for r in range(len(rocks)-1):
            for c in range(len(rocks[0])):
                if rocks[r][c]=='.' and rocks[r+1][c]=='O':
                    rocks[r][c], rocks[r+1][c] = rocks[r+1][c], rocks[r][c]
                    swap = True
    return rocks

def main():
    rocks = [[l for l in line] for line in get_input_lines()]
    rocks = shift_rocks(rocks)

    total = 0
    for r, row in enumerate(rocks):
        for c in row:
            if c == 'O':
                total += len(rocks)-r
    print(total)

if __name__=='__main__':
    main()