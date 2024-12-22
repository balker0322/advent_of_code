

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_d(c):
    if c=='^':
        return complex(-1, 0)
    if c=='>':
        return complex(0, 1)
    if c=='v':
        return complex(1, 0)
    if c=='<':
        return complex(0, -1)

def main():
    input_lines = get_input_lines()
    max_r = len(input_lines)
    max_c = len(input_lines[0])
    for r in range(max_r):
        for c in range(max_c):
            if input_lines[r][c] not in '.#':
                # print(r, c)
                pos = set([(r, c)])
                start_state = (complex(r, c), get_d(input_lines[r][c]))
                break

    while True:
        next_coor = start_state[0] + start_state[1]
        
        r = int(next_coor.real)
        c = int(next_coor.imag)
        # print(r, c)

        if r<0 or r>=max_r or c<0 or c>=max_c:
            print(len(pos))
            exit()


        if input_lines[r][c] == '#':
            start_state = (start_state[0], start_state[1]*complex('-j'))
            continue

        pos.add((r, c))
        
        start_state = (next_coor, start_state[1])


if __name__=='__main__':
    main()