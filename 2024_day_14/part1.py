import re

def get_next_pos(curr, step, v, total_tile):
    if v<0:
        v = total_tile+v
    next_pos = curr + v*step
    next_pos %= total_tile
    return next_pos

def main():

    r = 103
    c = 101
    mr, mc = int((r-1)/2), int((c-1)/2)
    step = 100
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in open(0).read().split('\n'):
        lc, lr, vc, vr = [int(x) for x in re.findall(r'\-?\d+', line)]
        nr, nc = get_next_pos(lr, step, vr, r), get_next_pos(lc, step, vc, c)
        if nr==mr or nc==mc:
            continue
        if nr>mr and nc>mc:
            q1+=1
            continue
        if nr>mr and nc<mc:
            q2+=1
            continue
        if nr<mr and nc>mc:
            q3+=1
            continue
        if nr<mr and nc<mc:
            q4+=1
            continue
    
    print(q1*q2*q3*q4)


if __name__=='__main__':
    main()