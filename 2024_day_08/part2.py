from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_all_comb(items:list):
    items = list(items)
    l = len(items)
    for i in range(l):
        for j in range(l):
            if i==j:
                continue
            yield (items[i], items[j])

def is_antenna(c):
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    valid_chars += valid_chars.upper()
    valid_chars += '0123456789'
    return c in valid_chars

def get_antinode(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = x1-x0
    dy = y1-y0
    return (x1+dx, y1+dy)
    
def main():
    input_lines = get_input_lines()
    nodes = {}
    max_r = len(input_lines)
    max_c = len(input_lines[0])

    antinodes = set([])

    for r in range(max_r):
        for c in range(max_c):
            node = input_lines[r][c]
            if not is_antenna(node):
                continue
            if node not in nodes:
                nodes[node] = set([])
            nodes[node].add((r, c))
            antinodes.add((r, c))
    
    for k, v in nodes.items():
        if len(v)==1:
            continue
        for p0, p1 in get_all_comb(v):
            while True:
                r, c = get_antinode(p0, p1)
                if r<0 or r>=max_r or c<0 or c>=max_c:
                    break
                # if (r, c) not in antinodes:
                #     print((r,c))
                antinodes.add((r, c))
                p0 = p1
                p1 = (r,c)
    
    

    # for r in range(max_r):
    #     row = ''
    #     for c in range(max_c):
    #         if (r,c) in antinodes:
    #             row+='#'
    #         else:
    #             row+='.'
    #     print(row)
    print(len(antinodes))

if __name__=='__main__':
    main()