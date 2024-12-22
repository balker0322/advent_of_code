import heapq

def get_min_step_with_path(sr, sc, er, ec, rows, cols, walls, path=tuple([]), skip_coor=None):
    if (sr, sc)==(er, ec): return 0, path+((sr, sc), )
    visited = set([])
    q = [(0, sr, sc, ((sr, sc),))]

    while q:
        node = heapq.heappop(q)
        d, r, c, path = node

        coor = (r, c)
        if coor in visited:
            continue

        visited.add(coor)

        for nr, nc in [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1),
        ]:
            nd = d+1
            n_path = path + ((nr, nc), )
            if (nr, nc) in visited:
                continue
            if (nr, nc)==(er, ec):
                return nd, n_path
            if nr<0 or nc<0 or nr>=rows or nc>=cols:
                continue
            if skip_coor:
                if (nr, nc)==skip_coor:
                    continue
            if (nr, nc) in walls:
                continue
            heapq.heappush(q, (nd, nr, nc, n_path))
        
    return None

cache = {}

# def get_min_step(sr, sc, er, ec, rows, cols, walls, skip_coor=None):
#     if (sr, sc)==(er, ec): return 0

#     global cache
    
#     key = (sr, sc, er, ec)
#     if key in cache:
#         return cache[key]

#     visited = set([])
#     q = [(0, sr, sc)]

#     while q:
#         node = heapq.heappop(q)
#         d, r, c = node

#         coor = (r, c)
#         if coor in visited:
#             continue

#         visited.add(coor)

#         for nr, nc in [
#             (r+1, c),
#             (r-1, c),
#             (r, c+1),
#             (r, c-1),
#         ]:
#             nd = d+1
#             if (nr, nc) in visited:
#                 continue
#             if (nr, nc)==(er, ec):
#                 cache[key] = nd
#                 return nd
#             if nr<0 or nc<0 or nr>=rows or nc>=cols:
#                 continue
#             if skip_coor:
#                 if (nr, nc)==skip_coor:
#                     continue
#             if (nr, nc) in walls:
#                 continue
#             heapq.heappush(q, (nd, nr, nc))

#     cache[key] = None   
#     return None

def get_min_step(sr, sc, er, ec, rows, cols, walls, skip_coor=None):
    if (sr, sc)==(er, ec): return 0

    global cache
    
    key = (sr, sc, er, ec)
    if key in cache:
        return cache[key]

    visited = set([])
    q = [(0, sr, sc)]

    while q:
        node = heapq.heappop(q)
        d, r, c = node

        coor = (r, c)
        if coor in visited:
            continue

        visited.add(coor)

        for nr, nc in [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1),
        ]:
            nd = d+1
            if (nr, nc) in visited:
                continue
            if (nr, nc)==(er, ec):
                cache[key] = nd
                return nd
            if nr<0 or nc<0 or nr>=rows or nc>=cols:
                continue
            if skip_coor:
                if (nr, nc)==skip_coor:
                    continue
            if (nr, nc) in walls:
                continue
            heapq.heappush(q, (nd, nr, nc))

    cache[key] = None   
    return None

def main():
    g = open(0).read().split('\n')
    rows = len(g)
    cols = len(g[0])

    walls = set([])
    cheats = set([])
    for r in range(rows):
        for c in range(cols):
            if g[r][c]=='S': sr, sc = r, c
            if g[r][c]=='E': er, ec = r, c
            if g[r][c]=='#': walls.add((r, c))

    orig_step, path = get_min_step_with_path(sr, sc, er, ec, rows, cols, walls)
    # print(sr, sc, er, ec)
    # print(path)
    # print(len(cheats))
    cheats = set([])
    for r, c in path:
        r1, c1 = r, c
        for r2, c2 in [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1),
        ]:
            if r2<0 or c2<0 or r2>=rows or c2>=cols:
                continue
            cheats.add(((r1, c1), (r2, c2)))
    
    # print(len(cheats))
    # exit()
    
    total = 0
    cheats_map = {}
    # cache = {}
    for i, cheat in enumerate(cheats):
        if (i+1)%100==0:
            print("{}/{}".format(i+1, len(cheats)))
        (r1, c1), (r2, c2) = cheat
        if len(set(cheat)&walls)==0:
            continue
        if (r1, c1)==(er, ec):
            continue
        r = get_min_step(sr, sc, r1, c1, rows, cols, walls, (er, ec))
        if r is None: continue
        d1 = r
        r = get_min_step(r2, c2, er, ec, rows, cols, walls)
        if r is None: continue
        d2 = r
        d = d1+d2+1
        saved = orig_step-d
        if saved<=0:
            continue
        cheats_map[saved] = cheats_map.get(saved, 0)+1
        if saved>=100:
            total += 1

    print(total)
    



if __name__=='__main__':
    main()