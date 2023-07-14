

def parse_string(s):
    tokens = s.split()
    x1, y1 = [int(n) for n in tokens[-3].split(',')]
    x2, y2 = [int(n) for n in tokens[-1].split(',')]
    method = ' '.join(tokens[:-3])
    return method, x1, y1, x2, y2


def get_input_list():
    input_list = None
    with open(r'2015_day_06\input.txt', 'r') as f:
        input_list = [line.strip() for line in f.readlines()]
    return input_list

def get_num_list(n1, n2):
    if n1<n2:
        return [i for i in range(n1, n2+1)]
    return [i for i in range(n1, n2-1, -1)]

def get_state(method, current_state):
    if 'turn on' in method:
        return 1
    if 'turn off' in method:
        return 0
    if current_state==1:
        return 0
    return 1

def main():

    input_list = get_input_list()
    input_list = [parse_string(s) for s in input_list]
    dimension = 1000

    lights = [[0 for _ in range(dimension)] for _ in range(dimension)]

    for method, x1, y1, x2, y2 in input_list:
        for x in get_num_list(x1, x2):
            for y in get_num_list(y1, y2):
                l = lights[x][y]
                lights[x][y] = get_state(method, l)


    ans = sum([sum([lights[x][y] for x in range(dimension)]) for y in range(dimension)])
    print(ans)


if __name__=='__main__':
    main()