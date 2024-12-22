from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

g_visited = set([])

def get_neighbor(item, d):
    (sr, sc), (er, ec) = item
    if sr==er:
        return (sr+d, sc), (er+d, ec)
    if sc==sc:
        return (sr, sc+d), (er, ec+d)


def get_perimeter(coors):
    
    vectors = set([])
    for r, c in coors:
        for nr, nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
            vectors.add(((r, c), (nr, nc)))
    
    out_vect = set([])
    for sc, ec in vectors:
        if (ec, sc) in vectors:
            continue
        out_vect.add((sc, ec))
    
    output = 0
    visited=set([])

    for item in out_vect:
        if item in visited:
            continue
        temp = tuple(item)
        while (temp:=get_neighbor(temp, 1)) in out_vect: visited.add(temp)
        temp = tuple(item)
        while (temp:=get_neighbor(temp, -1)) in out_vect: visited.add(temp)
        output += 1

    return output


def get_total_price(g, sr, sc):

    global g_visited

    if (sr, sc) in g_visited:
        return 0

    total_price = 0

    max_r, max_c = len(g), len(g[0])

    visited = set([])
    q = deque([(sr, sc)])
    n_list = set([])

    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        
        if g[r][c]==g[sr][sc]:
            for nr, nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                if nr<0 or nc<0 or nr>=max_r or nc>=max_c:
                    continue
                q.append((nr, nc))
            visited.add((r, c))
        else:
            n_list.add((r, c))
    
    g_visited |= visited
    
    for nr, nc in n_list:
        total_price += get_total_price(g, nr, nc)

    return total_price + len(visited)*get_perimeter(visited)


def main():
    il = get_input_lines()
    print(get_total_price(il, 0, 0))


if __name__=='__main__':
    main()