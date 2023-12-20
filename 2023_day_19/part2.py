from collections import deque

min_val, max_val = 1, 4000
p_index = {p:i for i, p in enumerate('xmas')}

def set_range_to_zero(masks, prl, mask_range)->tuple:
    new_masks = []
    for p in 'xmas':
        if p==prl:
            new_mask = list(masks[p_index[p]])
            a, b = mask_range
            for i in range(a, b+1):
                new_mask[i-1]=0
            new_masks.append(tuple(new_mask))
            continue
        new_masks.append(masks[p_index[p]])
    return tuple(new_masks)

def count_valid_val(valid_values):
    total = 1
    for pi in range(len('xmas')):
        sub=sum([i for i in valid_values[pi]])
        total*=sub
    return total
    

def main():
    wf, pr = [x.split('\n') for x in open(0).read().split('\n\n')]
    pr = [{r.split('=')[0]:int(r.split('=')[1]) for r in line[1:-1].split(',')} for line in pr]
    wf = [line.split('{') for line in wf]
    wf = {a:[c.split(':') for c in b[:-1].split(',')] for a, b in wf}
    
    q = deque([])
    visited = set([])

    q.appendleft((
        'in',
        tuple([tuple([1 for _ in range(max_val)]) for _ in range(len('xmas'))]),
        ('in',)
    ))

    total = 0
    total_r = 0

    while q:

        node = q.pop()

        if node in visited:
            continue
        
        label, masks, chain = node

        next_mask = tuple(masks)

        child_count = 0

        for nwf in wf[label]:

            if len(nwf)==1 and nwf[0]=='R':
                sub = count_valid_val(next_mask)
                total_r += sub
                continue

            if len(nwf)==1 and nwf[0]=='A':
                sub = count_valid_val(next_mask)
                total += sub
                continue

            if len(nwf)==1:
                q.appendleft((
                    nwf[-1],
                    next_mask,
                    tuple(list(chain)+[nwf[-1]]),
                ))
                continue
                
            cond, nl = nwf

            if '<' in cond:
                prl, num = cond.split('<')
                num = int(num)
                mask_range = (min_val, num-1)
                inv_mask_range = (num, max_val)
                true_mask = set_range_to_zero(next_mask, prl, inv_mask_range)
                false_mask = set_range_to_zero(next_mask, prl, mask_range)

            if '>' in cond:
                prl, num = cond.split('>')
                num = int(num)
                mask_range = (num+1, max_val)
                inv_mask_range = (min_val, num)
                true_mask = set_range_to_zero(next_mask, prl, inv_mask_range)
                false_mask = set_range_to_zero(next_mask, prl, mask_range)
            
            next_mask = tuple(false_mask)

            if nl=='A':
                sub = count_valid_val(true_mask)
                child_count+=sub
                total += sub
                continue

            if nl=='R':
                sub = count_valid_val(true_mask)
                total_r += sub
                continue

            q.appendleft((
                nl,
                tuple(true_mask),
                tuple(list(chain)+[nl])
            ))

        visited.add(node)
        
    print(total)


if __name__=='__main__':
    main()
