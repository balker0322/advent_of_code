
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def sr_to_se(s, r):
    return s, s+r-1

def se_to_sr(s, e):
    return s, e-s+1

def get_intersection(sa, ra, sb, rb):
    a1, a2 = sr_to_se(sa, ra)
    b1, b2 = sr_to_se(sb, rb)
    if b2 >= a1 and a2 >= b1:
        c1 = max(a1, b1)
        c2 = min(a2, b2)
        return se_to_sr(c1, c2)
    return None

def get_sub_comp(sa, ra, sb, rb):
    a1, a2 = sr_to_se(sa, ra)
    b1, b2 = sr_to_se(sb, rb)
    a = None
    b = None
    if b1 > a1:
        a = se_to_sr(a1, min(a2, b1-1))
    if a2 > b2:
        b = se_to_sr(max(a1, b2+1), a2)
    return a, b

def transform(iis, iir, s, d):
    ns = d + iis-s
    return ns, iir

def sort_list_by_source(val_list):
    sorted_list = []
    s_list = {v[1]:v for v in val_list}
    for k in sorted(list(s_list.keys())):
        sorted_list.append(s_list[k])
    return sorted_list

def get_split_range(sa, ra, sb, rb):
    a, c = get_sub_comp(sa, ra, sb, rb)
    b = get_intersection(sa, ra, sb, rb)
    return a, b, c

def main():

    map_val = {}
    for line in get_input_lines():
        if line.startswith('seeds:'):
            seed_val_list = [int(i) for i in line.split(':')[-1].split()]
            continue
        if ':' in line:
            s, _, d = line.split()[0].split('-')
            continue
        if line:
            if not s in map_val.keys():
                map_val[s] = [d, []]
            map_val[s][-1].append([int(i) for i in line.split()])
    
    result_list = []
    for a in zip(*[iter(seed_val_list)]*2):
        result_list.append(a)
    
    result_list = set(result_list)

    next_key = 'seed'

    while True:
        next_key, val_list = map_val[next_key]
        val_list = sort_list_by_source(val_list)

        new_r_list = []
        for ss, rr in result_list:
            for val in val_list:
                d, s, r = val
                os, ii, oe = get_split_range(ss, rr, s, r)
                if os:
                    new_r_list.append(os)
                if ii:
                    new_r_list.append(transform(*ii, s, d))
                if oe:
                    ss, rr = oe
                    continue
                break
            if oe:
                new_r_list.append(oe)
        result_list = list(new_r_list)
        
        if next_key=='location':
            break
    
    print(min([r[0] for r in result_list]))

if __name__=='__main__':
    main()