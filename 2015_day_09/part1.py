from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()

    graph = {}
    loc = set([])
    for line in input_lines:
        src, _, dst, _, dist = line.split()
        graph[(src, dst)] = int(dist)
        graph[(dst, src)] = int(dist)
        loc.add(src)
        loc.add(dst)
    
    q = deque()
    visited = set([])
    q.add(set([]))

    # while q:

    #     for n in 
    


if __name__=='__main__':
    main()