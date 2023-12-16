from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    grid = [[c for c in row] for row in input_lines]
    ncs = {
        'd':0-1j,
        'l':-1+0j,
        'u':0+1j,
        'r':1+0j,
    }
    ncs_inv = {v : k for k, v in ncs.items()}
    p90 = 1j
    n90 = -1j

    def traverse_laser(coor, dir):
        r, c = coor
        
        current_coor = r*(-1j)+c
        step = ncs[dir]
        next_coor_list = []
        current_tile = grid[r][c]

        next_coor = current_coor+step
        next_coor_list = [(next_coor)]
        if (current_tile=='-' and step.real==0) or (current_tile=='|' and step.imag==0):
            next_coor_list = [(current_coor+(step*p90)), (current_coor+(step*n90))]
        if (current_tile=='\\' and step.real==0) or (current_tile=='/' and step.imag==0):
            next_coor_list = [(current_coor+(step*p90))]
        if (current_tile=='\\' and step.imag==0) or (current_tile=='/' and step.real==0):
            next_coor_list = [(current_coor+(step*n90))]
        
        for next_coor in next_coor_list:
            next_dir = ncs_inv[next_coor-current_coor]
            yield ((int(-1*next_coor.imag), int(next_coor.real)), next_dir)
    
    max_result = 0

    starting_nodes = []
    starting_nodes += [((0, c), 'd') for c in range(len(grid[0]))]
    starting_nodes += [((len(grid)-1, c), 'u') for c in range(len(grid[0]))]
    starting_nodes += [((r, 0), 'r') for r in range(len(grid))]
    starting_nodes += [((r, len(grid[0])-1), 'l') for r in range(len(grid))]

    max_result = 0
    
    for start_node in starting_nodes:
        energized_grid = [['.' for _ in row] for row in input_lines]
        q = deque()
        q.appendleft(start_node)
        visited = set([])

        while q:
            next_node = q.pop()
            coor, dir = next_node

            for n_coor, n_dir in traverse_laser(coor, dir):
                nr, nc = n_coor
                if nr<0 or nc<0 or nr>len(grid)-1 or nc>len(grid[0])-1:
                    continue
                node = (n_coor, n_dir)
                if node in visited:
                    continue
                q.appendleft(node)
            visited.add(next_node)
            r, c = coor
            energized_grid[r][c] = '#'
        
        result = sum([sum([1 for c in row if c=='#']) for row in energized_grid])
        max_result = max(max_result, result)

    print(max_result)

if __name__=='__main__':
    main()