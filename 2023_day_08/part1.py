

def main():
    d, _g = open(0).read().split('\n\n')
    g = {}
    for gi in _g.split('\n'):
        a, b = gi.split(' = ')
        b = b.replace('(', '').replace(')', '').split(', ')
        g[a] = tuple(b)

    g_next = 'AAA'
    i = 0
    total_d = len(d)
    while True:
        if d[i%total_d]=='L':
            g_next = g[g_next][0]
        else:
            g_next = g[g_next][1]
        i+=1
        if g_next=='ZZZ':
            print(i)
            exit()


if __name__=='__main__':
    main()