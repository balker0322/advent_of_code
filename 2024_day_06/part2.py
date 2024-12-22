

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

def get_state_tuple(state):
    return tuple([int(state[0].real), int(state[0].imag), int(state[1].real), int(state[1].imag)])

def is_in_loop(grid, start_state, new_obs_coor):

    max_r = len(grid)
    max_c = len(grid[0])
    
    visited = set([])
    curr_state = tuple(start_state)

    while True:
        next_coor = curr_state[0] + curr_state[1]
        
        r = int(next_coor.real)
        c = int(next_coor.imag)

        if r<0 or r>=max_r or c<0 or c>=max_c:
            return False

        if grid[r][c] == '#' or (r, c)==new_obs_coor:
            curr_state = (curr_state[0], curr_state[1]*complex('-j'))
            continue

        state = get_state_tuple(curr_state)
        if state in visited:
            return True
        visited.add(state)
        
        curr_state = (next_coor, curr_state[1])


def main():
    input_lines = get_input_lines()
    max_r = len(input_lines)
    max_c = len(input_lines[0])
    for r in range(max_r):
        for c in range(max_c):
            if input_lines[r][c] not in '.#':
                start_state = (complex(r, c), get_d(input_lines[r][c]))
                break
    
    total = 0

    for r in range(max_r):
        for c in range(max_c):
            if (r, c) == (int(start_state[0].real), int(start_state[0].imag)):
                continue
            if input_lines[r][c] == '#':
                continue
            total += is_in_loop(input_lines, start_state, (r, c))
        
    print(total)

if __name__=='__main__':
    main()