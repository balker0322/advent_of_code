
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def str_to_int_list(s):
    return [int(x) for x in s]

def get_map(v):
    result = {}
    for d, s, r in v:
        dd = d
        ss = s
        for _ in range(r):
            result[ss] = dd
            dd+=1
            ss+=1
    return result


def is_val_in_map(val, map_val):
    for _, s, r in map_val:
        if val >= s:
            if val <= s + r:
                return True
    return False

def get_map_val(val, map_val):
    for d, s, r in map_val:
        if val >= s:
            if val <= s + r:
                return d+(val-s)
    
    return val
    

def main():
    input_lines = get_input_lines()

    info_dict = {}
    val_list = []
    next_key = None
    for line in input_lines:
        if line.startswith('seeds:'):
            seeds = line.split(':')[-1].split()
            seeds = str_to_int_list(seeds)
            continue
        if ':' in line:
            s,_,d = line.split()[0].split('-')
            next_key = (s, d)
            continue
        if line:
            val = str_to_int_list(line.split())
            val_list.append(val)
            continue
        if val_list:
            info_dict[next_key] = val_list
            val_list = list([])
        
    if val_list:
        info_dict[next_key] = val_list
    
    print('done info_dict')


    # create map
    map_conv_dict = {}
    for key, val in info_dict.items():
        s, d = key
        map_conv_dict[s] = (d, val)

    print('done map_conv_dict')
    
    next_source = 'seed'
    seeds_val_list = list(seeds)
    while True:
        d, map_val = map_conv_dict[next_source]
        new_val_list = []
        for val in seeds_val_list:
            new_val = val
            
            if is_val_in_map(val, map_val):
                new_val = get_map_val(val, map_val)

            # if val in map_val.keys():
            #     new_val = map_val[val]
            new_val_list.append(new_val)
        seeds_val_list = new_val_list
        next_source = d
        if next_source=='location':
            break
    
    print(min(seeds_val_list))



if __name__=='__main__':
    main()