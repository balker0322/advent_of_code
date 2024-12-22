import heapq
from collections import deque
import functools

npad = ['789', '456', '123', '#0A']
dpad = ['#^A', '<v>']
sdr, sdc, snr, snc = 0, 2, 3, 2

def get_next_coor(curr_r, curr_c, controller_state):
        next_r, next_c = curr_r, curr_c
        if controller_state=='^': next_r, next_c = curr_r-1, curr_c
        if controller_state=='<': next_r, next_c = curr_r, curr_c-1
        if controller_state=='>': next_r, next_c = curr_r, curr_c+1
        if controller_state=='v': next_r, next_c = curr_r+1, curr_c
        return next_r, next_c

def is_valid_dpad_coor(r, c):
    if r<0 or c<0 or r>=len(dpad) or c>=len(dpad[1]): return False
    if dpad[r][c]=='#': return False
    return True

def is_valid_coor(r, c, keypad):
    if r<0 or c<0 or r>=len(keypad) or c>=len(keypad[1]): return False
    if keypad[r][c]=='#': return False
    return True


def is_valid_npad_coor(r, c):
    if r<0 or c<0 or r>=len(npad) or c>=len(npad[1]): return False
    if npad[r][c]=='#': return False
    return True

@functools.lru_cache(maxsize=10000)
def get_next_state(move, nr, nc, *dpad_pos_list):
    ndpad_pos_list = []
    dpad_pos_list = deque(dpad_pos_list)
    dpad_in = move

    while dpad_pos_list:
        dpr = dpad_pos_list.popleft()
        dpc = dpad_pos_list.popleft()
        if dpad_in!='A':
            ndpr, ndpc = get_next_coor(dpr, dpc, dpad_in)
            if not is_valid_dpad_coor(ndpr, ndpc): return None
            ndpad_pos_list.append(ndpr)
            ndpad_pos_list.append(ndpc)
            ndpad_pos_list+=list(dpad_pos_list)
            return *ndpad_pos_list, nr, nc, ""
        dpad_in = dpad[dpr][dpc]
        ndpad_pos_list.append(dpr)
        ndpad_pos_list.append(dpc)

    if dpad_in!='A':
        nnpr, nnpc = get_next_coor(nr, nc, dpad_in)
        if not is_valid_npad_coor(nnpr, nnpc): return None
        return *ndpad_pos_list, nnpr, nnpc, ""
    return *ndpad_pos_list, nr, nc, npad[nr][nc]
    
def get_dpad_min_path(c):
    robot_count = 25
    q = [(0, *((sdr, sdc)*robot_count), snr, snc, "")]
    visited = set([])
    q = deque(q)

    while q:
        node = q.popleft()
        # node = heapq.heappop(q)

        # print(node)
        step, *dp_coor, npr, npc, code = node
        key = (*dp_coor, npr, npc, code)
        if key in visited: continue
        # visited.add((dr1, dc1, dr2, dc2, npr, npc, code))
        print(len(q), step, code)


        for n_move in '<^v>A':
            nstep = step+1
            result = get_next_state(n_move, npr, npc, *dp_coor)
            if result is None: continue
            *ndp_coor, nnpr, nnpc, next_code = result
            n_code = code + next_code
            if n_code==c:
                print(nstep)
                return nstep
            if len(n_code) > len(c): continue
            if not c.startswith(n_code): continue

            n_key = (*ndp_coor, nnpr, nnpc, n_code)
            if n_key in visited: continue

            new_node = (nstep, *n_key)
            q.append(new_node)
        
        
        visited.add(key)

    return 0

def get_complexity(c):
    l = get_dpad_min_path(c)
    return l*int(c[:-1])

# def solve(sr, sc, code, keypad):
#     q = deque([])
#     visited = set([])
#     q.append((sr, sc, '', ''))

#     min_step = float('inf')

#     solutions = []

#     while q:
#         # print(q)
#         node = q.popleft()
#         r, c, steps, sub_code = node

#         if node in visited: continue
#         # print(node)
#         for n_move in '<^v>A':
#             nsteps=steps+n_move
#             if len(nsteps)>min_step:
#                 continue
#             if n_move=='A':
#                 n_sub_code = sub_code+keypad[r][c]
#                 if sub_code==code:
#                     min_step = len(nsteps)
#                     solutions.append(nsteps)
#                     continue
#                 if code.startswith(n_sub_code):
#                     n_node = (r, c, nsteps, n_sub_code)
#                     if not n_node in visited: q.append(n_node)
#                 continue
#             nr, nc = get_next_coor(r, c, n_move)
#             if not is_valid_coor(nr, nc, keypad): continue
#             # print(nr, nc)
#             n_node = (nr, nc, nsteps, sub_code)
#             if not n_node in visited: q.append(n_node)
            
#         visited.add(node)
    
#     return solutions


def get_dist(start, end, keypad):
    if start==end:
        return ['A']
    
    coors = {}
    for r, row in enumerate(keypad):
        for c, item in enumerate(row):
            if item=='#':
                continue
            coors[item] = (r, c)
    
    solutions = []
    q = deque([(*(coors[start]), '')])
    min_dist = float('inf')
    visited = set([])

    while q:
        node = q.popleft()

        r, c, steps= node

        if node in visited: continue
        
        for n_move in '<^v>':
            nsteps = steps+n_move
            if len(nsteps)>min_dist:
                continue
            nr, nc = get_next_coor(r, c, n_move)
            if not is_valid_coor(nr, nc, keypad): continue
            if (nr, nc)==coors[end]:
                min_dist = len(nsteps)
                solutions.append(nsteps+'A')
                continue
            q.append((nr, nc, nsteps))

        visited.add(node)

    return set(solutions)

def get_dist_pairs(keypad):
    result = {}
    pad = set([])
    for r, row in enumerate(keypad):
        for c, item in enumerate(row):
            if item=='#':
                continue
            pad.add(item)
    for x in pad:
        for y in pad:
            result[(x, y)] = get_dist(x, y, keypad)
    return result

def get_min_pos(code, poss):
    if len(code)==2: return tuple(poss[(code[0], code[1])])
    pos = []
    for p in poss[(code[0], code[1])]:
        for pp in get_min_pos(code[1:], poss):
            pos += [p+pp]
    return tuple(set(pos))

dpad_pos = get_dist_pairs(dpad)
dpad_val = {key:len(list(val)[0]) for key, val in dpad_pos.items()}

@functools.cache
def solve(code, depth=25):
    if depth==1: return sum(dpad_val[(x, y)] for x, y in zip("A"+code, code))
    length = 0
    for a, b in zip("A"+code, code):
        length += min(solve(c, depth-1) for c in dpad_pos[(a, b)])
    return length

npad_pos = get_dist_pairs(npad)

def main():
    codes = open(0).read().split('\n')
    total=0
    for code in codes:
        l = min(solve(sc) for sc in get_min_pos('A'+code, npad_pos))
        print(l, code, get_min_pos('A'+code, npad_pos))
        total+=l*int(code[:-1])
    print(total)



if __name__=='__main__':
    main()