

def is_reflect(section_a, section_b):
    len_a = len(section_a)
    len_b = len(section_b)
    for i in range(min(len_a, len_b)):
        if section_a[-i-1]!=section_b[i]:
            return False
    return True


def get_h_line_reflect(pattern):

    for h_line in range(1, len(pattern)):
        section_a = pattern[:h_line]
        section_b = pattern[h_line:]
        if is_reflect(section_a, section_b):
            return h_line

    return 0

def transpose_pattern(pattern):
    new_pattern = []
    for i in range(len(pattern[0])):
        new_pattern.append(''.join([p[i] for p in pattern]))
    return new_pattern


def get_v_line_reflect(pattern):

    t_pattern = transpose_pattern(pattern)
    return get_h_line_reflect(t_pattern)


def main():

    pattern_list = []

    total = 0

    for pattern in open(0).read().split('\n\n'):
        p = []
        i=0
        for row in pattern.split('\n'):
            p.append(row)
            i+=1
        pattern_list.append(p)
        h = get_h_line_reflect(p)
        v = get_v_line_reflect(p)
        total += v + 100*h
    
    print(total)
    

if __name__=='__main__':
    main()