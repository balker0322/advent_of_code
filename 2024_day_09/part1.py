from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    space = deque([])
    is_file = True
    file_id = 0
    for n in input_lines[0]:
        n = int(n)
        item = None
        if is_file:
            item = file_id
            file_id += 1
        for _ in range(n):
            space.append(item)
        is_file = not is_file
    
    new_space = deque([])
    while space:
        item = space.popleft()
        if item is not None:
            new_space.append(item)
            continue
        if len(space) == 0:
            break
        while (last_item := space.pop()) is None:
            continue
        new_space.append(last_item)
    
    total = 0
    for i, n in enumerate(new_space):
        total += i*n

    print(total)

if __name__=='__main__':
    main()