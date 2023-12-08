from math import gcd

def get_lcm(num_list):
    lcm = 1
    for i in num_list:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def main():
    d, _g = open(0).read().split('\n\n')
    g = {}
    for gi in _g.split('\n'):
        a, b = gi.split(' = ')
        b = b.replace('(', '').replace(')', '').split(', ')
        g[a] = tuple(b)

    g_next_list = {gi:gi for gi in g.keys() if gi.endswith('A')}
    g_count = {}

    i = 0
    total_d = len(d)
    for g_start in g_next_list.keys():
        i = 0
        g_next = g_start
        while True:
            if d[i%total_d]=='L':
                g_next = g[g_next][0]
            else:
                g_next = g[g_next][1]
            i+=1
            if g_next.endswith('Z'):
                g_count[g_start] = i
                break
    
    result = get_lcm([x for x in g_count.values()])
    print(result)


if __name__=='__main__':
    main()