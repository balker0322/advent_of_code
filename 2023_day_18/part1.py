from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = [line.split() for line in get_input_lines()]
    input_lines = [(d, int(n), c[1:-1]) for d, n, c in input_lines]

    current_pos = (0, 0)
    path = set([])
    path.add(current_pos)
    for d, n, c in input_lines:
        for _ in range(n):
            pr, pc = current_pos
            if d=='D':
                current_pos = (pr+1, pc)
            if d=='L':
                current_pos = (pr, pc-1)
            if d=='U':
                current_pos = (pr-1, pc)
            if d=='R':
                current_pos = (pr, pc+1)
            # print(d, n, c, current_pos)
            path.add(current_pos)
    
    min_r = min([r for r, _ in path])
    max_r = max([r for r, _ in path])
    min_c = min([c for _, c in path])
    max_c = max([c for _, c in path])

    print(min_r, max_r, min_c, max_c)

    grid = [[(r, c) for c in range(min_c-1, max_c+2)] for r in range(min_r-1, max_r+2)]

    total_grid_count = sum([sum([1 for _ in row]) for row in grid])

    q = deque([])
    visited = set([])
    q.appendleft(grid[0][0])

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
            if nr<min_r-1 or nc<min_c-1 or nr>max_r+1 or nc>max_c+1:
                continue
            if (nr, nc) in path:
                continue
            q.appendleft((nr, nc))
        visited.add((r, c))
    
    print(total_grid_count - len(visited))


if __name__=='__main__':
    main()