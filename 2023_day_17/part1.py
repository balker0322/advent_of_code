from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_dir(straight_d):
    d_list = []
    d_list.append(straight_d)
    r, c = straight_d
    comp_d = c-(r*1j)
    p90 = comp_d*1j
    d_list.append((int(-1*p90.imag), int(p90.real)))
    n90 = comp_d*(-1j)
    d_list.append((int(-1*n90.imag), int(n90.real)))
    return d_list   


def build_graph(grid, starting_coor):
    q = deque([])
    q.appendleft((starting_coor, (0, 1), 1))
    q.appendleft((starting_coor, (1, 0), 1))

    graph = {}
    while q:
        node = q.pop()
        coor, d, dcount = node
        r, c = coor

        if node in graph.keys():
            continue

        neighbors = []
        for dr, dc in get_dir(d):
            nr = r+dr
            nc = c+dc
            if nr<0 or nc<0 or nr>len(grid)-1 or nc>len(grid[0])-1:
                continue
            ndcount = 1
            if (dr, dc)==d:
                ndcount = dcount+1
                if ndcount>3:
                    continue
            n_node = ((nr, nc), (dr, dc), ndcount)
            q.appendleft(n_node)
            neighbors.append(n_node)
        
        graph[node] = tuple(neighbors)

    return graph

def get_min_distance(graph, grid, starting_coor, end_coor):
    min_distance = float('inf')
    shortest_path = {x:float('inf') for x in graph.keys()}
    q = deque([])
    for node in [
        ((starting_coor, (0, 1), 1), 0),
        ((starting_coor, (1, 0), 1), 0),
    ]:
        _node, hl = node
        q.appendleft(node)
        shortest_path[_node] = 0
    visited = set([])

    while q:
        node, hl = q.pop()
        coor, d, dc = node
        r, c = coor

        if (node, hl) in visited:
            continue

        for nbr in graph[node]:
            nbr_coor, nbr_d, nbr_dc  = nbr
            nbr_r, nbr_c = nbr_coor

            shortest_path[nbr] = min(shortest_path[nbr], shortest_path[node]+grid[nbr_r][nbr_c])

            if nbr_coor==end_coor:
                min_distance = min(min_distance, shortest_path[nbr])
                continue
            
            if shortest_path[nbr] > min_distance:
                continue

            q.appendleft((nbr, shortest_path[nbr]))
        
        visited.add((node, hl))

    return min_distance


def main():
    input_lines = get_input_lines()
    grid = [[int(c) for c in line] for line in input_lines]
    starting_coor = (0, 0)
    end_coor = (len(grid)-1, len(grid[0])-1)

    graph = build_graph(grid, starting_coor)

    min_distance = get_min_distance(graph, grid, starting_coor, end_coor)
    print(min_distance)

if __name__=='__main__':
    main() 