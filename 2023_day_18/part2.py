from collections import deque
from itertools import product 

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_intersection_line(sq1, sq2):
    matched_p = []
    for p1 in sq1:
        for p2 in sq2:
            if p1==p2:
                matched_p.append(p1)
    if len(matched_p)==2:
        return tuple(matched_p)
    return None

def get_area(square):
    min_r = min([r for r, c in square])
    max_r = max([r for r, c in square])
    min_c = min([c for r, c in square])
    max_c = max([c for r, c in square])

    return (max_r-min_r+1)*(max_c-min_c+1)

def get_line_tile_count(line):
    
    min_r = min([r for r, c in line])
    max_r = max([r for r, c in line])
    min_c = min([c for r, c in line])
    max_c = max([c for r, c in line])

    return (max_r-min_r+1)*(max_c-min_c+1)
    

def main():
    input_lines = [line.split() for line in get_input_lines()]
    input_lines = [(d, int(n), c[1:-1]) for d, n, c in input_lines]

    current_pos = (0, 0)
    path_points = set([])
    path_points.add(current_pos)
    d_list = 'RDLU'

    r_grid_lines = set([])
    c_grid_lines = set([])
    border_lines = []

    for old_d, old_n, c in input_lines:
        d = d_list[int(c[-1])]
        n = int('0x'+c[1:6], 16)

        pr, pc = current_pos
        if d=='D':
            next_pos = (pr+n, pc)
        if d=='L':
            next_pos = (pr, pc-n)
        if d=='U':
            next_pos = (pr-n, pc)
        if d=='R':
            next_pos = (pr, pc+n)

        border_lines.append((current_pos, next_pos))
        current_pos = next_pos
        path_points.add(current_pos)
        r_grid_lines.add(current_pos[0])
        c_grid_lines.add(current_pos[1])

    r_grid_lines = sorted(r_grid_lines)
    c_grid_lines = sorted(c_grid_lines)
    border_lines = set(border_lines)
    old_border_lines = set(border_lines)

    for bl in old_border_lines:

        p1, p2 = bl
        grid_lines = None

        if p1[0]==p2[0]:
            a, b = min(p1[1], p2[1]), max(p1[1], p2[1])
            c = p1[0]
            g_points = set([])
            for g in c_grid_lines:
                if a<=g<=b:
                    g_points.add(g)
            for g1, g2 in product(g_points, repeat=2):
                border_lines.add(((c, g1), (c, g2)))

        if p1[1]==p2[1]:
            a, b = min(p1[0], p2[0]), max(p1[0], p2[0])
            c = p1[1]
            g_points = set([])
            for g in r_grid_lines:
                if a<=g<=b:
                    g_points.add(g)
            for g1, g2 in product(g_points, repeat=2):
                border_lines.add(((g1, c), (g2, c)))
    
    
    border_lines = set(border_lines)
    old_border_lines = set(border_lines)

    for a, b in old_border_lines:
        border_lines.add((b, a))

    grid_squares = []

    r_grid_lines = [r_grid_lines[0]-100] + r_grid_lines + [r_grid_lines[-1]+100]
    c_grid_lines = [c_grid_lines[0]-100] + c_grid_lines + [c_grid_lines[-1]+100]

    for r in range(len(r_grid_lines)-1):
        row = []
        for c in range(len(c_grid_lines)-1):
            square = [
                (r_grid_lines[r], c_grid_lines[c]),
                (r_grid_lines[r], c_grid_lines[c+1]),
                (r_grid_lines[r+1], c_grid_lines[c+1]),
                (r_grid_lines[r+1], c_grid_lines[c]),
            ]
            row.append(tuple(square))
        grid_squares.append(row)
        

    q = deque([])
    visited = set([])
    q.appendleft((0, 0))

    while q:
        r, c = q.pop()

        if (r, c) in visited:
            continue

        for dr, dc in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]:
            nr, nc = r+dr, c+dc
            if nr<0 or nc<0 or nr>len(grid_squares)-1 or nc>len(grid_squares[0])-1:
                continue

            p1, p2 = get_intersection_line(grid_squares[r][c], grid_squares[nr][nc])
            
            if (p1, p2) in border_lines or (p2, p1) in border_lines:
                continue

            q.appendleft((nr, nc))
        visited.add((r, c))

    covered_squares_coor = set([])
    for r in range(len(grid_squares)):
        for c in range(len(grid_squares[0])):
            if (r, c) in visited:
                continue
            covered_squares_coor.add((r, c))

    area = 0
    counted_edges = set([])
    counted_corners = set([])
    for r, c in covered_squares_coor:
        square = grid_squares[r][c]
        area+=get_area(square)
        area-=4 # remove corner tiles

        for p in square:
            if not p in counted_corners:
                area += 1
            counted_corners.add(p)

        a, b, c, d = square

        for line in [
            (a, b),
            (b, c),
            (c, d),
            (d, a),
        ]:
            if line in counted_edges:
                area-=get_line_tile_count(line)
                area+=2
            p1, p2 = line
            counted_edges.add((p1, p2))
            counted_edges.add((p2, p1))

    print(area)

if __name__=='__main__':
    main()