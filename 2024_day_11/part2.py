from collections import deque

def get_input():
    return [line.strip() for line in open(0).readlines()][0].split()

mem = {}

def get_stone_count(depth, stone):
    key = (depth, stone)
    if key in mem:
        return mem[key]
    if depth==0:
        result = 1
    elif stone==0:
        result = get_stone_count(depth-1, 1)
    else:
        s = str(stone)
        l = len(s)
        if l%2==0:
            l = int(l/2)
            result = get_stone_count(depth-1, int(s[:l])) + get_stone_count(depth-1, int(s[l:]))
        else:
            result = get_stone_count(depth-1, stone*2024)
    mem[key]=result
    return result


def main():
    blink = 75
    inp = tuple(map(int, get_input()))
    print(sum(get_stone_count(blink, stone) for stone in inp))


if __name__=='__main__':
    main()