from collections import deque

# SF-|.LJ7
up = '|LJ'
down = '|F7'
left = '-7J'
right = '-FL'

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
        g.append(tuple(row))

    g = tuple(g)
    
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
    # print(max_d)
    # print(min([x[0] for x in loop_tiles]))
    # print(min([x[1] for x in loop_tiles]))
    # print(max([x[0] for x in loop_tiles]))
    # print(max([x[1] for x in loop_tiles]))
    # print(max_r)
    # print(max_c)
    # exit()

    q = deque(list(loop_tiles))
    covered_loop_tiles = set([])

    sr, sc = start_coor
    # SF-|.LJ7
    for r in range(max_r):
        is_inside = False
        for c in range(max_c):
            pass

    # while q:
    #     c_node = q.pop()
    #     r, c = c_node
    #     for dr, dc in [
    #         (-1, 0),
    #         (1, 0),
    #         (0, 1),
    #         (0, -1),
    #     ]:
    #         nr = r+dr
    #         nc = c+dc
    #         if (nr, nc) in covered_loop_tiles:
    #             continue
    #         if nr < 0 or nr >= max_r or nc < 0 or nc >= max_c:
    #             continue
    #         if (nr, nc) in loop_tiles:
    #             continue
    #         q.appendleft((nr, nc))
            
    #     covered_loop_tiles.add(c_node)
    
    print('done identifying covered_loop_tiles', len(covered_loop_tiles))
    print_node(covered_loop_tiles, max_r, max_c, g)

    print(len(covered_loop_tiles) - len(loop_tiles))






if __name__=='__main__':
    main()