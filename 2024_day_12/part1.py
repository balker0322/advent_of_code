from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

g_visited = set([])

def get_total_price(g, sr, sc):
    global g_visited

    if (sr, sc) in g_visited:
        return 0

    total_price = 0
    area = 0
    perimeter = 0

    visited = set([])
    q = deque([])
    q.append((sr, sc))
    n_tiles = set([])

    while q:
        r, c = q.pop()

        if (r, c) in visited:
            continue

        if g[r][c]==g[sr][sc]:
            for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                if nr<0 or nc<0 or nr>=len(g) or nc>=len(g[0]):
                    perimeter+=1
                    continue
                q.append((nr, nc))
                if g[nr][nc]!=g[sr][sc]:
                    perimeter+=1
            area += 1
            visited.add((r, c))
        else:
            n_tiles.add((r, c))

    total_price = 0
    g_visited |= visited

    for r, c in n_tiles:
        total_price +=  get_total_price(g, r, c)

    return total_price + area*perimeter

def main():
    il = get_input_lines()
    print(get_total_price(il, 0, 0))


if __name__=='__main__':
    main()