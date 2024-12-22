import re
from collections import deque

def main():

    max_step = 100
    total_token = 0

    for block in open(0).read().split('\n\n'):
        ax, ay, bx, by, px, py = [int(x) for x in re.findall(r'\d+', block)]

        q = deque([])
        visited = set([])
        q.append((0, 0, 0, 0))
        token = None

        while q:
            state = q.pop()

            if state in visited:
                continue

            x, y, ac, bc = state

            for nx, ny, nac, nbc in [(x+ax, y+ay, ac+1, bc), (x+bx, y+by, ac, bc+1)]:
                if nac>max_step or nbc>max_step or nx>px or ny>py:
                    continue
                t = 3*nac + nbc
                if token is not None:
                    if t > token:
                        continue
                if nx==px and ny==py:
                    if token is None:
                        token = t
                    else:
                        token = min(t, token)
                    continue
                q.append((nx, ny, nac, nbc))
        
            visited.add(state)
        
        if token is not None:
            total_token += token
        
    print(total_token)


if __name__=='__main__':
    main()