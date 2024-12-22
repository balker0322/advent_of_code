from collections import deque

def main():
    rules, _ = open(0).read().split('\n\n')

    max_num = 4000

    rule_map = {}
    for line in rules.split('\n'):
        line
        label, line = line.split('{')
        line = line.replace('}', '')
        r = line.split(',')
        items = []
        for ri in r[:-1]:
            a, b = ri.split(':')
            if '<' in a: op='<'
            if '>' in a: op='>'
            v_label, val = a.split(op)
            val = int(val)
            items.append((v_label, op, val, b))
        items.append(r[-1])
        rule_map[label] = items
        print(label, items)

    q = deque([])
    visited = set([])
    all_flag = set([i+1 for i in range(max_num)])
    state = ('in', all_flag , all_flag , all_flag , all_flag )
    q.append(state)

    ans = []

    while q:
        node = q.pop()

        if node in visited:
            continue

        label, x, m, a, s = node

        for ni, n_node in enumerate(rule_map[label]):
            # print(n_node)

            if ni==len(rule_map[label])-1:
                n_label=n_node
                if n_label=='R':
                    continue
                if n_label=='A':
                    ans.append((x, m, a, s))
                    continue
                q.append((n_label, x, m, a, s))
                continue

            c, op, val, n_label = n_node
            if n_label=='A':
                ans.append((x, m, a, s))
                continue
            if n_label=='R':
                continue

            all_flag = set([i+1 for i in range(max_num)])
            if op=='>':
                true_flag = set([i+1 for i in range(max_num) if i+1>val])
            if op=='<':
                true_flag = set([i+1 for i in range(max_num) if i+1<val])
            false_flag = all_flag-true_flag

            nx, nm, na, ns = x, m, a, s
            if c=='x': nx &= true_flag
            if c=='m': nm &= true_flag
            if c=='a': na &= true_flag
            if c=='s': ns &= true_flag
            q.append((n_label, nx, nm, na, ns))

            nx, nm, na, ns = x, m, a, s
            if c=='x': nx &= false_flag
            if c=='m': nm &= false_flag
            if c=='a': na &= false_flag
            if c=='s': ns &= false_flag
            q.append((n_label, nx, nm, na, ns))

        visited.add(node)
    
    print(ans)


if __name__=='__main__':
    main()