

def main():

    keypad = ['123', '456', '789']
    max_r = len(keypad)
    max_c = len(keypad[0])
    coor = {}
    for ir in range(max_r):
        for ic in range(max_c):
            coor[keypad[ir][ic]] = (ir, ic)

    r, c = coor['5']
    for line in open(0).read().split('\n'):
        for letter in line:
            nr, nc = r, c
            if letter=='D': nr = r+1
            if letter=='L': nc = c-1
            if letter=='U': nr = r-1
            if letter=='R': nc = c+1
            
            if nr>=0 and nr<max_r: r = nr
            if nc>=0 and nc<max_c: c = nc
        print(keypad[r][c], end='')
                


if __name__=='__main__':
    main()