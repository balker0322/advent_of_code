from random import randint

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

def iter_h_line_reflect(pattern):

    for h_line in range(1, len(pattern)):
        section_a = pattern[:h_line]
        section_b = pattern[h_line:]
        if is_reflect(section_a, section_b):
            yield h_line

def transpose_pattern(pattern):
    new_pattern = []
    for i in range(len(pattern[0])):
        new_pattern.append(''.join([p[i] for p in pattern]))
    return new_pattern

def get_v_line_reflect(pattern):

    t_pattern = transpose_pattern(pattern)
    return get_h_line_reflect(t_pattern)

def apply_smudge(pattern, rr, rc):
    new_pattern = []
    for r, row in enumerate(pattern):
        new_row = ''
        for c, item in enumerate(row):
            new_item = item
            if (r, c)==(rr, rc):
                if item=='.':
                    new_item='#'
                else:
                    new_item='.'
            new_row+=new_item
        new_pattern.append(new_row)
    return new_pattern

def iter_coor(pattern):
    for r in range(len(pattern)):
        for c in range(len(pattern[0])):
            yield r, c

def main():

    total = 0
    p_count = 0

    for pattern in open(0).read().split('\n\n'):
        p_count+=1
        p = []
        for row in pattern.split('\n'):
            p.append(row)

        mirrors = set([])

        for h in iter_h_line_reflect(p):
            mirrors.add((h, 0))

        for v in iter_h_line_reflect(transpose_pattern(p)):
            mirrors.add((0, v))

        new_mirrors = set([])

        for r, c in iter_coor(p):
            smudged_p = apply_smudge(p,r,c)

            for h in iter_h_line_reflect(smudged_p):
                new_mirrors.add((h, 0))

            for v in iter_h_line_reflect(transpose_pattern(smudged_p)):
                new_mirrors.add((0, v))
        
        for h,v in new_mirrors.difference(mirrors):
            total += h*100 + v

    print(total)
    

if __name__=='__main__':
    main()