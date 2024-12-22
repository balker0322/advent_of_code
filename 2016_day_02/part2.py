

def main():

    keypad = [
        '.......',
        '...1...',
        '..234..',
        '.56789.',
        '..ABC..',
        '...D...',
        '.......',
    ]
    max_r = len(keypad)
    max_c = len(keypad[0])
    coor = {}
    for ir in range(max_r):
        for ic in range(max_c):
            key = keypad[ir][ic]
            if key=='.':
                continue
            coor[key] = (ir, ic)

    r, c = coor['5']
    for line in open(0).read().split('\n'):
        for letter in line:
            nr, nc = r, c
            if letter=='D': nr = r+1
            if letter=='L': nc = c-1
            if letter=='U': nr = r-1
            if letter=='R': nc = c+1
            
            # print(letter, keypad[nr][nc], (nr, nc))
            if keypad[nr][nc]=='.':
                continue
            r, c = nr, nc
        print(keypad[r][c], end='')
                

if __name__=='__main__':
    main()