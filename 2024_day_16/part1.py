from collections import deque

def cw(r, c):
    x = complex(r, c)*complex('j')
    return (int(x.real), int(x.imag))

def ccw(r, c):
    x = complex(r, c)*complex('-j')
    return (int(x.real), int(x.imag))

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
                previous[v] = None
                q.add(v)
    score[s] = 0

    visited = set([])

    while q:
        # print(len(q))
        min_score = float('inf')
        min_v = None
        for v in q:
            if score[v] < min_score:
                min_score = score[v]
                min_v = v
        (r, c), (dr, dc) = min_v

        for nv, n_score in [
            (((r+dr, c+dc),(dr, dc)),1),
            (((r, c),cw(dr, dc)),1000),
            (((r, c),ccw(dr, dc)),1000),
        ]:
            if nv in visited: continue
            (nr, nc), _ = nv
            if g[nr][nc]=='#': continue
            temp_score = min_score + n_score
            if temp_score<score[nv]:
                score[nv] = temp_score
                previous[nv] = min_v
        
        visited.add(min_v)
        q.remove(min_v)
    
    return score, previous
    
def main():
    g = open(0).read().split('\n')
    rows = len(g)
    cols = len(g[0])
    
    for r in range(rows):
        for c in range(cols):
            t = g[r][c]
            if t=='S':
                s=(r,c)
                continue
            if t=='E':
                e=(r,c)
                continue
    
    d = (0, 1)
    scores, _ = dijkstra(g, (s, d))
    print(min([s for ((r, c), _), s in scores.items() if g[r][c]=='E']))
    
if __name__=='__main__':
    main()