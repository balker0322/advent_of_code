
def print_map(max_r, max_c, boxes, walls, curr_pos):
    lb = set([x for x, _ in boxes])
    rb = set([x for _, x in boxes])
    for _ in range(10): print()
    for r in range(max_r):
        for c in range(max_c):
            tile = '.'
            if (r, c) in lb: tile = '['
            if (r, c) in rb: tile = ']'
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
            c = 2*c
            if val=='@':
                curr_pos = (r, c)
                continue
            if val=='#':
                walls.add((r, c))
                walls.add((r, c+1))
                continue
            if val=='O':
                boxes.add(((r, c), (r, c+1)))

    for d in enumerate(dirs):
        if d=='^': dr, dc = -1, 0
        if d=='>': dr, dc = 0, 1
        if d=='<': dr, dc = 0, -1
        if d=='v': dr, dc = 1, 0

        r, c = curr_pos
        nr, nc = r+dr, c+dc

        if (nr, nc) in walls:
            continue

        stack = []

        if (b:=((nr, nc), (nr, nc+1))) in boxes: stack.append(b)
        if (b:=((nr, nc-1), (nr, nc))) in boxes: stack.append(b)

        free_to_move = True
        visited = set([])

        while stack:
            b = stack.pop()
            (r, c), _ = b
            nr, nc = r+dr, c+dc

            if {(nr, nc), (nr, nc+1)}&walls:
                free_to_move = False
                break
            
            other_boxes = boxes-{b}
            for nb in [
                ((nr, nc), (nr, nc+1)),
                ((nr, nc-1), (nr, nc)),
                ((nr, nc+1), (nr, nc+2)),
            ]:
                if not nb in other_boxes:
                    continue
                if nb in visited:
                    continue
                stack.append(nb)

            visited.add(b)

        if free_to_move:
            new_box_pos = set([((r+dr, c+dc), (r+dr, c+dc+1)) for (r, c), _ in visited])
            boxes -= visited
            boxes |= new_box_pos
            r, c = curr_pos
            nr, nc = r+dr, c+dc
            curr_pos = (nr, nc)

    # print_map(len(pos), len(pos[0])*2, boxes, walls, curr_pos)
    print(sum(100*r+c for (r, c), _ in boxes))

if __name__=='__main__':
    main()