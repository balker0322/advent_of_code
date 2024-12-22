import heapq


def print_graph(rows, cols, bytes):
    for r in range(rows):
        for c in range(cols):
            if (c, r) in bytes:
                print('#', end='')
                continue
            print('.', end='')
        print()


def main():
    (rows, cols), *bytes = [tuple(map(int, l.split(','))) for l in open(0).read().split('\n')]
    n = 12
    if rows>=70:
        n = 1024
    bytes = set(bytes[:n])

    sr, sc, er, ec = 0, 0, rows, cols
    rows, cols = rows+1, cols+1

    # print_graph(rows, cols, bytes)
    # exit()

    q = []
    visited = set([])
    q.append((0, sr, sc))

    while q:
        node = heapq.heappop(q)
        if node in visited:
            continue
        visited.add(node)

        score, r, c = node

        for nr, nc in [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1),
        ]:
            if nr<0 or nc<0 or nr>=rows or nc>=cols:
                continue
            if (nc, nr) in bytes:
                continue
            new_node = (score+1, nr, nc)
            if new_node in visited:
                continue
            if (nr, nc) == (er, ec):
                print(score+1)
                exit()
            heapq.heappush(q, new_node)


if __name__=='__main__':
    main()