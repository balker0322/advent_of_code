from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    
    space = deque([])
    is_file = True
    file_id = 0
    for n in input_lines[0]:
        n = int(n)
        item = None
        if is_file:
            item = file_id
            file_id += 1
        for _ in range(n):
            space.append(item)
        is_file = not is_file
        
    ip = len(space) - 1
    while ip >= 0:
        
        while space[ip] is None:
            ip-=1
            continue

        data = space[ip]
        data_len = 1
        while space[ip - data_len]==data:
            data_len+=1
            continue

        ips = 0
        cons_none_cnt = 0
        while ips < ip-data_len+1:
            if space[ips] is None:
                cons_none_cnt += 1
            else:
                cons_none_cnt = 0
            
            if cons_none_cnt==data_len:
                for i in range(data_len):
                    space[ips - i] = data
                    space[ip - i] = None
                break
            ips += 1
        
        ip = ip-data_len

    total = 0
    for i, n in enumerate(space):
        if n is None:
            continue
        total += i*n

    print(total) 

if __name__=='__main__':
    main()