from collections import deque

def is_possible(patterns, design:str):
    q = deque([])
    visited = set([])
    q.append(design)

    while q:
        node = q.pop()
        if node in visited:
            continue
        
        sub_d = node

        for pat in patterns:
            if sub_d.startswith(pat):
                n_node = sub_d[len(pat):]
                if n_node=="": return True
                q.append(n_node)

        visited.add(node)
    
    return False

def main():
    patterns, designs = open(0).read().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.split('\n')

    print(sum(is_possible(patterns, d) for d in designs))


if __name__=='__main__':
    main()