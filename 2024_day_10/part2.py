from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_score(g, s):

    peaks = set([])

    q = deque([])
    visited = set([])
    q.append(tuple([s]))

    while q:
        item = q.popleft()
        
        if item in visited:
            continue
        r, c = item[-1]

        if g[r][c]==9:
            peaks.add(item)
            continue

        for dr, dc in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]:
            nr, nc = r+dr, c+dc
            if nr<0 or nc<0 or nr>=len(g) or nc>=len(g[0]):
                continue
            if g[nr][nc]==g[r][c]+1:
                q.append(item+((nr, nc), ))
    
        visited.add(item)
                
    return len(peaks)

def main():
    input_lines = get_input_lines()
    g = list(map(lambda row: list(map(int, row)),input_lines))

    zeros = set([])
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c]==0:
                zeros.add((r, c))
    
    total = 0
    for s in zeros:
        total += get_score(g, s)
    
    print(total)

    

if __name__=='__main__':
    main()