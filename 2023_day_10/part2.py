from collections import deque

# SF-|.LJ7
up = '|LJ'
down = '|F7'
left = '-7J'
right = '-FL'

sides = {
    'F':([(-1,-1), (-1,0), (0,-1)], [(1,1)]),
    'L':([(1,-1), (1,0), (0,-1)], [(-1,1)]),
    'J':([(1,1), (1,0), (0,1)], [(-1,-1)]),
    '7':([(-1,1), (-1,0), (0,1)], [(1,-1)]),
    '|':([(0,-1)], [(0,1)]),
    '-':([(-1,0)], [(1,0)]),
}

connections = {
    'F':((1,0), (0,1)),
    'L':((-1,0),(0,1)),
    'J':((-1,0),(0,-1)),
    '7':((1,0),(0,-1)),
    '|':((-1,0),(1,0)),
    '-':((0,1),(0,-1)),
}

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_neighbors(node, g, max_r, max_c):
    coor, visited_tiles = node
    visited_tiles = set(visited_tiles)
    r, c = coor
    c_item = g[r][c]
    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]:
        nr = r+dr
        nc = c+dc
        if nr < 0 or nr >= max_r or nc < 0 or nc >= max_c:
            continue
        n_item = g[nr][nc]
        if n_item=='.':
            continue
        if c_item=='S':
            if ((dr, dc)==(-1, 0) and n_item in down) \
            or ((dr, dc)==(1, 0) and n_item in up) \
            or ((dr, dc)==(0, -1) and n_item in right) \
            or ((dr, dc)==(0, 1) and n_item in left):
                print(dr, dc, c_item, n_item)
                visited_tiles.add(coor)
                yield (nr, nc), tuple(visited_tiles)
            continue
        if n_item=='S':
            visited_tiles.add(coor)
            yield (nr, nc), tuple(visited_tiles)
            continue
        if (nr, nc) in visited_tiles:
            continue
        if c_item in up and n_item in down and (dr, dc)==(-1, 0):
            visited_tiles.add(coor)
            yield (nr, nc), tuple(visited_tiles)
            continue
        if c_item in down and n_item in up and (dr, dc)==(1, 0):
            visited_tiles.add(coor)
            yield (nr, nc), tuple(visited_tiles)
            continue
        if c_item in left and n_item in right and (dr, dc)==(0, -1):
            visited_tiles.add(coor)
            yield (nr, nc), tuple(visited_tiles)
            continue
        if c_item in right and n_item in left and (dr, dc)==(0, 1):
            visited_tiles.add(coor)
            yield (nr, nc), tuple(visited_tiles)
            continue

def print_node(node, max_r, max_c, g):
    # return
    visited_tiles = node
    print()
    for r in range(max_r):
        row = []
        for c in range(max_c):
            if (r,c) in visited_tiles:
                row.append(g[r][c])
                continue
            row.append('@')
        print(row)
    
def print_n(coor, n, g):
    s = g[coor[0]][coor[1]]
    d = g[n[0]][n[1]]
    if n[0]==1 and n[1]==0:
        print(s, '->', d)



def main():
    input_lines = get_input_lines()
    g = []
    # s = set([])
    for r, line in enumerate(input_lines):
        row = []
        for c, item in enumerate(line):
            # s.add(item)
            if item=="S":
                start_coor = (r, c)
            row.append(item)
        g.append(row)

    
    max_r = len(g)
    max_c = len(g[0])
    d = 0
    q = deque([])
    visited = set([])
    q.appendleft((start_coor, tuple(set([]))))
    max_d = d
    while q:
        c_node = q.pop()
        # print_node(c_node, max_r, max_c)
        for n in get_neighbors(c_node, g, max_r, max_c):
            if n in visited:
                # print('n in visited')
                continue
            # visited.add(c_node[1])
            coor, visited_tile = n
            # print_n(c_node[0], n[0], g)
            if coor == start_coor:
                # max_d = max(max_d, len(visited_tile))
                d = len(visited_tile)
                if d > max_d:
                    # print_node(n, max_r, max_c, g)
                    max_d = d
                    loop_tiles = set(visited_tile)
                continue
            q.appendleft(n)
        visited.add(c_node)
    
    print('total', max_r*max_c)
    print('done identifying loop', len(loop_tiles))
    print_node(loop_tiles, max_r, max_c, g)


    # get outside coor
    q = deque([])
    for r in range(max_r):
        for c in range(max_c):
            if r==0 or r==max_r-1 or c==0 or c==max_c-1:
                if (r,c) in loop_tiles:
                    continue
                q.appendleft((r, c))
    outside_coors = set([])
    while q:
        c_node = q.pop()
        r, c = c_node
        for dr, dc in [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=max_r or nc<0 or nc>=max_c:
                continue
            n_node = (nr, nc)
            if n_node in outside_coors:
                continue
            if n_node in loop_tiles:
                continue
            q.appendleft(n_node)
        outside_coors.add(c_node)

    print('done outside_coors')
    print_node(outside_coors, max_r, max_c, g)



    sr, sc = start_coor
    g[sr][sc] = '7'

    new_start_found = False
    for r, c in loop_tiles:
        for dr, dc in [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]:
            nr = r+dr
            nc = c+dc
            if (nr, nc) in outside_coors:
                new_start_found = True
                nsr, nsc = r, c
                break
        if new_start_found:
            break

    print(start_coor, (nsr, nsc))

    q = deque([])
    q.appendleft((nsr, nsc))
    visited = set([])
    inside_coor = set([])
    orig_outside_coor = set(outside_coors)
    path_seq = []

    while q:
        c_node = q.pop()
        r,c = c_node
        c_val = g[r][c]
        for dr, dc in connections[c_val]:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=max_r or nc<0 or nc>=max_c:
                continue
            n_node = (nr, nc)
            if n_node in visited:
                continue
            side_a, side_b = sides[c_val]

            side_out = side_b
            side_in = side_a
            for sr, sc in side_a:
                if (sr, sc) in outside_coors:
                    side_out = side_a
                    side_in = side_b
                    break
            
            for sr, sc in side_out:
                outside_coors.add((nr+sr, nc+sc))
            for sr, sc in side_in:
                if (nr+sr, nc+sc) in orig_outside_coor:
                    continue
                inside_coor.add((nr+sr, nc+sc))
            
            q.appendleft(n_node)
            break

        path_seq.append(c_node)
        visited.add(c_node)
    

    c_node = path_seq[0]
    r, c = c_node
    c_val = g[r][c]
    d_side_a, d_side_b = sides[c_val]
    
    side_a = set([])
    for dr, dc in d_side_a:
        side_a.add((r+dr, c+dc))
    side_b = set([])
    for dr, dc in d_side_b:
        side_b.add((r+dr, c+dc))

    side_outer = side_b
    side_inner = side_a
    if len(side_a.intersection(orig_outside_coor)):
        side_outer = side_a
        side_inner = side_b

    inner_coors = set([])

    for r, c in side_inner:
        node = (r,c)
        if node in loop_tiles:
            continue
        inner_coors.add(node)
    
    def expand_set(a):
        new_a = set([])
        for r, c in a:
            new_a.add((r, c))
            for dr, dc in [
                (0,1),
                (0,-1),
                (1,0),
                (-1,0)
            ]:
                new_a.add((r+dr, c+dc))
        return new_a

    for i in range(len(path_seq)-1):
        c_side_inner, c_side_outer = side_inner, side_outer

        r, c = path_seq[i+1]
        c_val = g[r][c]
        d_side_a, d_side_b = sides[c_val]
        
        side_a = set([])
        for dr, dc in d_side_a:
            side_a.add((r+dr, c+dc))
        side_b = set([])
        for dr, dc in d_side_b:
            side_b.add((r+dr, c+dc))
        
        side_outer = side_b
        side_inner = side_a
        if len(side_a.intersection(expand_set(c_side_outer))):
            side_outer = side_a
            side_inner = side_b
        
        for r, c in side_inner:
            node = (r,c)
            if node in loop_tiles:
                continue
            inner_coors.add(node)

    print('initial inner_coors')
    print_node(inner_coors, max_r, max_c, g)

    q = deque([])
    for node in inner_coors:
        q.appendleft(node)
    visited = set([])
    while q:
        c_node = q.pop()
        r, c = c_node
        for dr, dc in [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=max_r or nc<0 or nc>=max_c:
                continue
            n_node = (nr, nc)
            if n_node in visited:
                continue
            if n_node in loop_tiles:
                continue
            q.appendleft(n_node)
        visited.add(c_node)
    
    print(len(visited))
            


if __name__=='__main__':
    main()