
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_power(info):
    fewest_count = {
        'red':0,
        'green':0,
        'blue':0,
    }
    for rev_cycle in info.split(';'):
        for ball_info in rev_cycle.split(','):
            count, color = ball_info.split()
            count = int(count)
            fewest_count[color] = max(fewest_count[color], count)
    
    result = 1
    for c in fewest_count.values():
        result *= c
    
    return result

def main():
    input_lines = get_input_lines()
    total = 0
    for line in input_lines:
        info = line.split(':')[-1]
        total += get_power(info)
    print(total)

if __name__=='__main__':
    main()