def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    num_list = '0123456789'
    g = []
    for line in get_input_lines():
        r = []
        for i in line:
            r.append(i)
        g.append(r)

    
    num = ''
    key = []
    num_map = {}
    for ri, r in enumerate(g):
        for ci, c in enumerate(r):
            if c in num_list:
                num += c
                key.append((ri, ci))
                continue
            if num:
                num_map[tuple(key)] = int(num)
            num = ''
            key = []

    total = 0
    for ri, r in enumerate(g):
        for ci, c in enumerate(r):
            if c == '*':
                neighbors = set([])
                for rr, cc in [
                    (ri, ci+1),
                    (ri, ci-1),
                    (ri+1, ci+1),
                    (ri+1, ci-1),
                    (ri+1, ci),
                    (ri-1, ci+1),
                    (ri-1, ci-1),
                    (ri-1, ci),
                ]:
                    for key in num_map.keys():
                        if (rr, cc) in key:
                            neighbors.add(key)
                            break
                if len(neighbors) == 2:
                    gr = 1
                    for n in neighbors:
                        gr*=num_map[n]
                    total += gr
    
    print(total)

if __name__=='__main__':
    main()