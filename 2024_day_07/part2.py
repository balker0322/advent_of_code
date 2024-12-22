from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def concat(a, b):
    a = str(a)
    b = str(b)
    return int(a+b)

def is_match(t, n):
    n0, *nl = n
    q = deque([(n0, tuple(nl))])
    while q:
        rt, tnl = q.pop()
        if len(tnl):
            x = tnl[0]
            q.append((rt+x, tnl[1:]))        
            q.append((rt*x, tnl[1:]))     
            q.append((concat(rt,x), tnl[1:]))     
            continue
        if t==rt:
            return True
    return False

def main():
    input_lines = get_input_lines()
    total = 0
    for line in input_lines:
        t, *n = line.split()
        t = int(t.replace(':', ''))
        n = [int(i) for i in n]
        if is_match(t, n):
            total += t
    print(total)

if __name__=='__main__':
    main()