

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_guess(guess_size, hash_count_req):
    for i in range(2**guess_size):
        bin_str = str(bin(i))[2:]
        bin_str = '0'*(guess_size-len(bin_str))+bin_str
        if sum([1 if n=='1' else 0 for n in bin_str])==hash_count_req:
            yield ''.join(['#' if n=='1' else '.' for n in bin_str])

def guess_is_valid(data, guess_val, qm_index, info):
    data = list(data)
    guess_val = list(guess_val)
    assert len(guess_val) == len(qm_index)
    for qi in qm_index:
        data[qi]=guess_val.pop()
    calc = tuple([len(x) for x in ''.join(data).split('.') if len(x)])
    cond = calc==tuple(info)
    if cond:
        # print(''.join(data), calc, tuple(info), cond)
        return True
    return False

def get_arr_count(data, info):
    qm_count = sum([1 if x=='?' else 0 for x in data])
    hash_count = sum([1 if x=='#' else 0 for x in data])
    qm_index = tuple([i for i, d in enumerate(data) if d=='?'])
    arr_count = 0
    for guess_val in get_guess(qm_count, sum(info)-hash_count):
        if guess_is_valid(data, guess_val, qm_index, info):
            arr_count+=1
    return arr_count


def main():
    input_lines = get_input_lines()
    total = 0
    for line in input_lines:
        data, info = line.split()
        info = tuple(map(int, info.split(',')))
        total+=get_arr_count(data, info)
        # break
    
    print(total)

if __name__=='__main__':
    main()
    # for i in get_guess(3,2):
    #     print(i)