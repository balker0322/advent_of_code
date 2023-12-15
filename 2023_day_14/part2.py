
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def print_rock(rocks):
    print()
    for row in rocks:
        print(''.join(row))

def shift_left(rocks):
    rocks = list(list(r) for r in rocks)
    swap = True
    while swap:
        swap=False
        for r in range(len(rocks)):
            for c in range(len(rocks[0])-1):
                if rocks[r][c]=='.' and rocks[r][c+1]=='O':
                    rocks[r][c], rocks[r][c+1] = rocks[r][c+1], rocks[r][c]
                    swap = True
    return tuple(tuple(r) for r in rocks)

def shift_right(rocks):
    rocks = list(list(r) for r in rocks)
    swap = True
    while swap:
        swap=False
        for r in range(len(rocks)):
            for c in range(len(rocks[0])-1):
                if rocks[r][c]=='O' and rocks[r][c+1]=='.':
                    rocks[r][c], rocks[r][c+1] = rocks[r][c+1], rocks[r][c]
                    swap = True
    return tuple(tuple(r) for r in rocks)

def shift_up(rocks):
    rocks = list(list(r) for r in rocks)
    swap = True
    while swap:
        swap=False
        for r in range(len(rocks)-1):
            for c in range(len(rocks[0])):
                if rocks[r][c]=='.' and rocks[r+1][c]=='O':
                    rocks[r][c], rocks[r+1][c] = rocks[r+1][c], rocks[r][c]
                    swap = True
    return tuple(tuple(r) for r in rocks)

def shift_down(rocks):
    rocks = list(list(r) for r in rocks)
    swap = True
    while swap:
        swap=False
        for r in range(len(rocks)-1):
            for c in range(len(rocks[0])):
                if rocks[r][c]=='O' and rocks[r+1][c]=='.':
                    rocks[r][c], rocks[r+1][c] = rocks[r+1][c], rocks[r][c]
                    swap = True
    return tuple(tuple(r) for r in rocks)

memory = {}

def shift_rocks(d, rocks):

    result = None
    if d=='up':
        result = shift_up(rocks)
    if d=='down':
        result = shift_down(rocks)
    if d=='right':
        result = shift_right(rocks)
    if d=='left':
        result = shift_left(rocks)

    return result

def cycle_rocks(rocks, n=1):

    global memory

    key = (rocks, n)

    if key in memory.keys():
        return memory[key]

    for _ in range(n):
        sub_key = (rocks, 1)
        if sub_key in memory.keys():
            rocks = memory[sub_key]
            continue
        rocks = shift_rocks('up', rocks)
        rocks = shift_rocks('left', rocks)
        rocks = shift_rocks('down', rocks)
        rocks = shift_rocks('right', rocks)
        memory[sub_key] = rocks

    memory[key] = rocks

    return rocks

def get_load(rocks):
    total = 0
    for r, row in enumerate(rocks):
        for c in row:
            if c == 'O':
                total += len(rocks)-r
    return total


def main():
    rocks = tuple([tuple([l for l in line]) for line in get_input_lines()])
    
    i = 1000000000
    while i:
        n = 100000
        rocks = cycle_rocks(rocks, n)
        i -= n

    total = get_load(rocks)
    print(total)

if __name__=='__main__':
    main()