import re
import time

def get_next_pos(curr, step, v, total_tile):
    if v<0:
        v = total_tile+v
    next_pos = curr + v*step
    next_pos %= total_tile
    return next_pos

def get_new_state(robots, r, c, step=1):
    new_state = []
    occ = set([])
    for lc, lr, vc, vr in robots:
        nr, nc = get_next_pos(lr, step, vr, r), get_next_pos(lc, step, vc, c)
        new_state.append((nc, nr, vc, vr))
        occ.add((nr, nc))
    return new_state, occ

def display_state(state, r, c):
    for ir in range(r):
        for ic in range(c):
            tile='.'
            if (ir, ic) in state:
                tile='*'
            print(tile, end='')
        print()

def is_tree_found(state):
    for ir, ic in state:
        tree_tiles = set([
            (ir, ic),
            (ir+1, ic),
            (ir+1, ic-1),
            (ir+1, ic+1),
            (ir+2, ic),
            (ir+2, ic-1),
            (ir+2, ic+1),
            (ir+2, ic-2),
            (ir+2, ic+2),
        ])
        if tree_tiles.issubset(state):
            return True
    return False

def main():
    
    r = 103
    c = 101

    robots = tuple([(int(x) for x in re.findall(r'\-?\d+', line)) for line in open(0).read().split('\n')])

    iter_count = 1
    while True:
        robots, state = get_new_state(robots, r, c)
        if is_tree_found(state):
            display_state(state, r, c)
            print(iter_count)
            exit()
        iter_count += 1

if __name__=='__main__':
    main()