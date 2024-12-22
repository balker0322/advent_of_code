from collections import deque

def cw(r, c):
    x = complex(r, c)*complex('j')
    return (int(x.real), int(x.imag))

def ccw(r, c):
    x = complex(r, c)*complex('-j')
    return (int(x.real), int(x.imag))

def print_graph(path, walls, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if (r, c) in walls:
                print('#', end='')
                continue
            if (r, c) in path:
                print('O', end='')
                continue
            print('.', end='')
        print()

def dijkstra(g, s):

    rows = len(g)
    cols = len(g[0])
    _, (dr, dc) = s

    score = {}
    previous = {}
    q = set([])
    for r in range(rows):
        for c in range(cols):
            if g[r][c]=='#': continue
            for v in [
                ((r, c), (0, 1)),
                ((r, c), (0, -1)),
                ((r, c), (1, 0)),
                ((r, c), (-1, 0)),
            ]:
                score[v] = float('inf')
                previous[v] = []
                q.add(v)
    score[s] = 0

    while q:
        min_score = float('inf')
        min_v = None
        for v in q:
            if score[v] < min_score:
                min_score = score[v]
                min_v = v
        q.remove(min_v)
        (r, c), (dr, dc) = min_v

        for nv, n_score in [
            (((r+dr, c+dc),(dr, dc)),1),
            (((r, c),cw(dr, dc)),1000),
            (((r, c),ccw(dr, dc)),1000),
        ]:
            if not nv in q: continue
            (nr, nc), _ = nv
            if g[nr][nc]=='#': continue
            temp_score = min_score + n_score
            if temp_score<=score[nv]:
                score[nv] = temp_score
                previous[nv].append(min_v)
        
    return score, previous
               
def main():
    g = open(0).read().split('\n')
    rows = len(g)
    cols = len(g[0])
    
    walls = set([])
    for r in range(rows):
        for c in range(cols):
            t = g[r][c]
            if t=='#':
                walls.add((r,c))
                continue
            if t=='S':
                s=(r,c)
                continue
            if t=='E':
                e=(r,c)
                continue
    
    d = (0, 1)
    scores, previous = dijkstra(g, (s, d))
    min_score=min([s for ((r, c), _), s in scores.items() if g[r][c]=='E'])
    print(min_score)

    paths = set([])

    q = deque([])

    for key, val_list in previous.items():
        if scores[key] != min_score:
            continue
        (r, c), _ = key
        if (r, c) != e:
            continue
        for val in val_list:
            q.append(val)

    visited = set([])
    paths = set([s, e])

    while q:
        node = q.popleft()
        (r, c), _ = node

        if node in visited:
            continue

        for n_node in previous[node]:
            q.append(n_node)

        visited.add(node)
        paths.add((r, c))
    
    print(len(paths))

    exit()

    (sr, sc), (dr, dc) = s, d
    start_node = ((sr, sc, dr, dc, 0), (s, ))

    q = deque([])
    visited = set([])
    q.append(start_node)
    min_score = float('inf')
    end_collections = set([])

    while q:
        # print(len(q))
        node = q.popleft()

        if node in visited:
            continue
        
        # print(node)
        (r, c, dr, dc, score), path = node

        for n_node in [
            (r+dr, c+dc, dr, dc, score+1), 
            (r, c, *cw(dr, dc), score+1000), 
            (r, c, *ccw(dr, dc), score+1000),
        ]:
            nr, nc, ndr, ndc, nscore = n_node
            if (nr, nc) in walls:
                continue
            if nscore>min_score:
                continue
            new_node = (n_node, tuple(set(path+((nr, nc), ))))
            if (nr, nc) == e:
                min_score = min(min_score, nscore)
                end_collections.add(new_node)
                continue
            q.append(new_node)

        visited.add(node)

    # print(min_score)
    paths = set([])
    for node in end_collections:
        (r, c, dr, dc, score), path = node
        if score == min_score:
            # print((r, c, dr, dc, score), path)
            paths |= set(path)
        
    # print(len(end_collections))


    print(len(paths))
    # print_graph(paths, walls, rows, cols)
    
if __name__=='__main__':
    main()