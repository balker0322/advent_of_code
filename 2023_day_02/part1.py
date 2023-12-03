
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_req():
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    return {
        'red':12,
        'green':13,
        'blue':14,
    }

def main():
    input_lines = get_input_lines()
    req = get_req()
    total = 0
    for line in input_lines:
        label, info = line.split(':')
        id = int(label.split()[-1])
        line_valid = True
        for rev_cycle in info.split(';'):
            for ball_info in rev_cycle.split(','):
                count, color = ball_info.split()
                if int(count) > req[color]:
                    line_valid = False
                    break
        if not line_valid:
            continue
        total += id
    print(total)

if __name__=='__main__':
    main()