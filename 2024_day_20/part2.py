from collections import deque

def get_possible_n(r, c, rows, cols, radius):
    results = []

    for rad in range(0, radius+1):
        for dr in range(rad+1):
            dc = rad - dr
            for nr, nc in [
                (r+dr, c+dc),
                (r-dr, c+dc),
                (r-dr, c-dc),
                (r+dr, c-dc),
            ]:
                results.append((nr, nc, rad))
    return set(results)

def main():
    g = open(0).read().split('\n')
    rows = len(g)
    cols = len(g[0])

    # print(50, 50)
    # for r, c, rad in get_possible_n(50, 50, 100, 100, 2):
    #     if rad<2:
    #         continue
    #     print(rad, r, c)
    # print(len(get_possible_n(50, 50, 100, 100, 2)))
    # exit()


    walls = set([])
    for r in range(rows):
        for c in range(cols):
            if g[r][c]=='S': sr, sc = r, c
            if g[r][c]=='E': er, ec = r, c
            if g[r][c]=='#': walls.add((r, c))
    

    dists = [[-1]*cols for _ in range(rows)]
    q = deque([(sr, sc)])
    dists[sr][sc] = 0
    visited = set([])

    while q:
        r, c = q.pop()
        if (r, c) in visited: continue
        for nr, nc in [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1),
        ]:
            if nr<0 or nc<0 or nr>=rows or nc>=cols:
                continue
            if (nr, nc) in walls:
                continue
            if (nr, nc) in visited:
                continue
            dists[nr][nc] = dists[r][c]+1
            q.append((nr, nc))
        visited.add((r, c))

    total = 0
    coors = set([])
    cheat_map = {}
    for r in range(rows):
        for c in range(cols):
            if (r, c) in walls:
                continue

            for nr, nc, rad in get_possible_n(r, c, rows, cols, 20):
                if rad < 2:
                    continue
                if nr<0 or nc<0 or nr>=rows or nc>=cols:
                    continue
                if (nr, nc) in walls:
                    continue
                diff = dists[nr][nc] - dists[r][c]
                if dists[nr][nc] - dists[r][c] >= 100 + rad:
                    total+=1
                    coors.add((r, c, nr, nc))
                cheat_map[diff-rad] = cheat_map.get(diff-rad, 0)+1
    print_dic = lambda key, ref: print(key, cheat_map[key], ref, cheat_map[key]==ref)

    # for k, v in cheat_map.items():
    #     if k>0:
    #         print(k, v)

    # print_dic(2, 14)
    # print_dic(4, 14)
    # print_dic(6, 2)
    # print_dic(8, 4)
    # print_dic(10, 2)
    # print_dic(12, 3)
    # print_dic(20, 1)
    # print_dic(36, 1)
    # print_dic(38, 1)
    # print_dic(40, 1)
    # print_dic(64, 1)

    # exit()
    # print_dic(50, 32)
    # print_dic(52, 31)
    # print_dic(54, 29)
    # print_dic(56, 39)
    # print_dic(58, 25)
    # print_dic(60, 23)
    # print_dic(62, 20)
    # print_dic(64, 19)
    # print_dic(66, 12)
    # print_dic(68, 14)
    # print_dic(70, 12)
    # print_dic(72, 22)
    # print_dic(74, 4 )
    # print_dic(76, 3 )

# "There are 32 cheats that save 50 picoseconds."
# "There are 31 cheats that save 52 picoseconds."
# "There are 29 cheats that save 54 picoseconds."
# "There are 39 cheats that save 56 picoseconds."
# "There are 25 cheats that save 58 picoseconds."
# "There are 23 cheats that save 60 picoseconds."
# "There are 20 cheats that save 62 picoseconds."
# "There are 19 cheats that save 64 picoseconds."
# "There are 12 cheats that save 66 picoseconds."
# "There are 14 cheats that save 68 picoseconds."
# "There are 12 cheats that save 70 picoseconds."
# "There are 22 cheats that save 72 picoseconds."
# "There are 4 cheats that save  74 picoseconds."
# "There are 3 cheats that save  76 picoseconds."
    print(total, len(coors))

if __name__=='__main__':
    main()