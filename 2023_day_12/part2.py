

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def is_fit(data, info):
    if info[0]>len(data):
        return False
    for i in range(info[0]):
        if data[i]=='.':
            return False
    if len(data)==info[0]:
        return True
    if data[info[0]]=='#':
        return False
    return True

def get_all_valid_pos(data, info):

    for i in range(len(data)):
        if '#' in data[:i]:
            break
        temp_data = list(data)
        for j in range(info[0]):
            if i+j>len(data)-1:
                break
            if data[i+j]=='?':
                temp_data[i+j]='#'
        temp_data = ''.join(temp_data).replace('?', '.')
        if not is_fit(temp_data[i:], info):
            continue
        yield data[i+info[0]+1:], info[1:]
 
memory = {}   

def get_arr_count(data, info):

    global memory

    key = (data, tuple(info))
    if key in memory.keys():
        return memory[key]

    if len(info)==0:
        if all([d!='#' for d in data]):
            return 1
        return 0
    
    if len(data)==0:
        return 0

    arr_count = 0

    for next_data, next_info in get_all_valid_pos(data, info):
        arr_count += get_arr_count(next_data, next_info)
    
    memory[key] = arr_count
    return arr_count

    
def main():
    input_lines = get_input_lines()
    mul = 5
    total = 0
    loop_count = 0
    for line in input_lines:
        loop_count+=1
        data, info = line.split()
        info = tuple(map(int, info.split(',')))
        data = '?'.join([data]*mul)
        info = tuple(list(info)*mul)
        arr_count = get_arr_count(data, info)
        # print(loop_count, arr_count, line)
        total += arr_count
    print(total)
    

if __name__=='__main__':
    main()