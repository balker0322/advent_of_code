import heapq
from collections import deque

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

def is_valid_npad_coor(r, c):
    if r<0 or c<0 or r>=len(npad) or c>=len(npad[1]): return False
    if npad[r][c]=='#': return False
    return True
     
def get_dpad_min_path(c):
    q = [(0, sdr, sdc, sdr, sdc, snr, snc, "")]
    visited = set([])
    q = deque(q)

    while q:
        node = q.popleft()
        # node = heapq.heappop(q)
        if node in visited:
            continue
        # print(node)
        step, dr1, dc1, dr2, dc2, npr, npc, code = node
        # visited.add((dr1, dc1, dr2, dc2, npr, npc, code))

        for n_move in '<^v>A':
            nstep, ndr1, ndc1, ndr2, ndc2, nnpr, nnpc, ncode = step, dr1, dc1, dr2, dc2, npr, npc, code
            nstep = step+1
            if n_move!='A':
                ndr1, ndc1 = get_next_coor(dr1, dc1, n_move)
                if not is_valid_dpad_coor(ndr1, ndc1): continue
            else:
                dpad1_out = dpad[dr1][dc1]
                if dpad1_out!='A':
                    ndr2, ndc2 = get_next_coor(dr2, dc2, dpad1_out)
                    if not is_valid_dpad_coor(ndr2, ndc2): continue
                else:
                    dpad2_out = dpad[dr2][dc2]
                    if dpad2_out!='A':
                        nnpr, nnpc = get_next_coor(npr, npc, dpad2_out)
                        if not is_valid_npad_coor(nnpr, nnpc): continue
                    else:
                        npad_out = npad[npr][npc]
                        ncode = code+npad_out
                        if len(ncode) > len(c): continue
                        if ncode==c:
                            print(nstep)
                            return nstep

            key = (dr1, ndc1, ndr2, ndc2, nnpr, nnpc, ncode)
            if key in visited: continue

            new_node = (nstep, ndr1, ndc1, ndr2, ndc2, nnpr, nnpc, ncode)
            # heapq.heappush(q, new_node)
            q.append(new_node)
        
        
        visited.add((dr1, dc1, dr2, dc2, npr, npc, code))


    return 0

def get_complexity(c):
    l = get_dpad_min_path(c)
    return l*int(c[:-1])

def main():
    codes = open(0).read().split('\n')
    # get_complexity(codes[0])
    print(sum(get_complexity(c) for c in codes))

if __name__=='__main__':
    main()