from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()

    graph = {}
    loc_list = set([])
    for line in input_lines:
        src, _, dst, _, dist = line.split()
        if not src in graph.keys():
            graph[src] = {}
        if not dst in graph.keys():
            graph[dst] = {}
        graph[src][dst] =  int(dist)
        graph[dst][src] =  int(dist)
        loc_list.add(src)
        loc_list.add(dst)

    loc = {l:i for i, l in enumerate(loc_list)}

    q = deque()
    q.append((''.join(['0' for _ in loc]), None, 0))
    visited = set([])
    max_dist = float('-inf')

    while q:

        curr_node = q.pop()
        vmark, curr, td = curr_node

        if curr_node in visited:
            continue
        
        visited.add((vmark, curr, td))

        if not curr:
            for l in loc.keys():
                q.append((vmark, l, td))
            continue

        nvmark = list(vmark)
        nvmark[loc[curr]] = '1'
        nvmark = ''.join(nvmark)

        if sum([int(m) for m in nvmark]) == len(loc_list):
            max_dist = max(max_dist, td)
            continue

        for nloc, d in graph[curr].items():
            mark = loc[nloc]
            if vmark[mark] == '1':
                continue
            q.append((nvmark, nloc, td+d))
    
    print(max_dist)

if __name__=='__main__':
    main()