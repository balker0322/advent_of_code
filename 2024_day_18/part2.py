import heapq

def print_graph(rows, cols, bytes):
    for r in range(rows):
        for c in range(cols):
            if (c, r) in bytes:
                print('#', end='')
                continue
            print('.', end='')
        print()

def is_passable(sr, sc, er, ec, rows, cols, bytes):
    q = []
    visited = set([])
    q.append((0, sr, sc))

    while q:
        node = heapq.heappop(q)

        score, r, c = node

        if (r, c) in visited:
            continue
        visited.add((r, c))


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
            if (nr, nc) in visited:
                continue
            if (nr, nc) == (er, ec):
                return score+1
            heapq.heappush(q, new_node)

    return None
    
def main():
    (rows, cols), *bytes = [tuple(map(int, l.split(','))) for l in open(0).read().split('\n')]

    sr, sc, er, ec = 0, 0, rows, cols
    rows, cols = rows+1, cols+1

    for n in range(len(bytes)):
        _bytes = set(bytes[:n])
        score = is_passable(sr, sc, er, ec, rows, cols, _bytes)
        if score is None:
            print(*bytes[n-1], sep=',')
            exit()

if __name__=='__main__':
    main()