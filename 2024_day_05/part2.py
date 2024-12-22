
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def is_correct_order(rules, _nl):
    ord_d = {n:i for i, n in enumerate(_nl)}
    for a, b in rules:
        if a in _nl and b in _nl:
            if ord_d[a] > ord_d[b]:
                return False
    return True

def fix_order(rules, _nl):
    new_nl = list(_nl)
    ord_d = {n:i for i, n in enumerate(new_nl)}
    while True:
        is_correct_order = True                        
        for a, b in rules:
            if a in _nl and b in _nl:
                if ord_d[a] > ord_d[b]:
                    new_nl[ord_d[a]], new_nl[ord_d[b]] = new_nl[ord_d[b]], new_nl[ord_d[a]]
                    ord_d = {n:i for i, n in enumerate(new_nl)}
                    is_correct_order = False
                    break
        if is_correct_order:
            return new_nl

def get_mid_num(nl):
    return nl[int(len(nl)/2)]

def main():
    input_lines = get_input_lines()               
    sec1, sec2 = '_'.join(input_lines).split('__')
    sec1 = [list([int(y) for y in x.split('|')]) for x in sec1.split('_')]
    sec2 = [[int(y) for y in x.split(',')] for x in sec2.split('_')]

    total = 0
    for nl in sec2:
        if not is_correct_order(sec1, nl):
            new_nl = fix_order(sec1, nl)
            total += get_mid_num(new_nl)
        
    print(total)

if __name__=='__main__':
    main()
