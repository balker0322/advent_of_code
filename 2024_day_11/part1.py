from collections import deque

def get_input():
    return [line.strip() for line in open(0).readlines()][0].split()

def main():
    blink = 25

    q = deque(get_input())
    for _ in range(blink):
        new_q = deque([])
        while q:
            s = q.popleft()
            if s=='0':
                new_q.append('1')
                continue
            sl = len(s)
            if sl%2==0:
                hsl = int(sl/2)
                new_q.append(str(int(s[:hsl])))
                new_q.append(str(int(s[hsl:])))
                continue
            new_q.append(str(int(s)*2024))
        q = deque(list(new_q))
    
    print(len(q))




if __name__=='__main__':
    main()