
def is_valid_inc_seq(seq:list):
    if len(seq)==1:
        return True
    n1, n2 = seq[0], seq[1]
    if n2-n1>3:
        return False
    if n2-n1<1:
        return False
    return is_valid_inc_seq(list(seq[1:]))

def is_safe(seq):
    if seq[0] > seq[1]:
        seq.reverse()
    return is_valid_inc_seq(seq)

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    print(sum([is_safe([int(n) for n in line.split()]) for line in input_lines]))

if __name__=='__main__':
    main()