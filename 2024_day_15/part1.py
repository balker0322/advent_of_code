
def print_map(max_r, max_c, boxes, walls, curr_pos):
    print()
    for r in range(max_r):
        for c in range(max_c):
            tile = '.'
            if (r, c) in boxes: tile = 'O'
            if (r, c) in walls: tile = '#'
            if (r, c) == curr_pos: tile = '@'
            print(tile, end='')
        print()
        

def main():
    pos, dirs = open(0).read().split('\n\n')
    dirs = dirs.replace('\n', '')
    pos = pos.split('\n')

    boxes = set([])
    walls = set([])

    for r in range(len(pos)):
        for c in range(len(pos[0])):
            val = pos[r][c]
            if val=='@': curr_pos = (r, c)
            if val=='#': walls.add((r, c))
            if val=='O': boxes.add((r, c))


    for d in dirs:
        if d=='^': dr, dc = -1, 0
        if d=='>': dr, dc = 0, 1
        if d=='<': dr, dc = 0, -1
        if d=='v': dr, dc = 1, 0

        stack = [curr_pos]

        while True:
            r, c = stack[-1]
            nr, nc = r+dr, c+dc
            if (nr, nc) in boxes:
                stack.append((nr, nc))
                continue
            break

        while stack:
            r, c = stack.pop()
            nr, nc = r+dr, c+dc
            if (nr, nc) in walls:
                continue
            if (nr, nc) in boxes:
                continue
            if len(stack)==0:
                curr_pos = (nr, nc)
                continue
            boxes.remove((r, c))
            boxes.add((nr, nc))
        
    # print_map(len(pos), len(pos[0]), boxes, walls, curr_pos)
    print(sum(100*r+c for r, c in boxes))

if __name__=='__main__':
    main()