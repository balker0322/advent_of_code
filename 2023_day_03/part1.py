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

    total = 0
    num = ''
    adj_sym_found = False

    for ri, r in enumerate(g):
        for ci, c in enumerate(r):
            if c in num_list:
                num += c
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
                    if adj_sym_found:
                        break
                    if rr < 0 or rr >= len(g) or cc < 0 or cc >= len(r):
                        continue
                    if g[rr][cc] in num_list:
                        continue
                    if g[rr][cc] != '.':
                        adj_sym_found = True
                continue
            if num:
                if adj_sym_found:
                    total += int(num)
                num = ''
                adj_sym_found = False
    
    print(total)




if __name__=='__main__':
    main()