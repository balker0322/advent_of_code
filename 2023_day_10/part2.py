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
    _, visited_tiles = node
    print()
    for r in range(max_r):
        row = []
        for c in range(max_c):
            if (r,c) in visited_tiles:
                row.append(g[r][c])
                continue
            row.append('.')
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
                    # print(d, visited_tile)
                continue
            q.appendleft(n)
        visited.add(c_node)

    print(int(max_d/2))


if __name__=='__main__':
    main()