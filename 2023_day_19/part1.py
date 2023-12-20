

def get_next_wf(p, wf):
    for step in wf[:-1]:
        cond, next_wf = step
        if '<' in cond:
            v, num = cond.split('<')
            if p[v] < int(num):
                return next_wf
        if '>' in cond:
            v, num = cond.split('>')
            if p[v] > int(num):
                return next_wf
    return wf[-1][0]
        

def main():
    wf, pr = [x.split('\n') for x in open(0).read().split('\n\n')]
    pr = [{r.split('=')[0]:int(r.split('=')[1]) for r in line[1:-1].split(',')} for line in pr]
    wf = [line.split('{') for line in wf]
    wf = {a:[c.split(':') for c in b[:-1].split(',')] for a, b in wf}

    total = 0
    for p in pr:
        current_wf = 'in'
        while True:
            current_wf = get_next_wf(p, wf[current_wf])
            if current_wf == 'A':
                total += sum([val for val in p.values()])
                break
            if current_wf == 'R':
                break
    print(total)


if __name__=='__main__':
    main()