
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def is_x_mas(g, coor):
    r, c = coor
    
    if g[r][c] != 'A':
        return False
    
    if r-1<0 or c-1<0 or r+1>=len(g) or c+1>=len(g[0]):
        return False
    
    cond1 = (g[r-1][c-1]=='M' and g[r+1][c+1]=='S') or (g[r-1][c-1]=='S' and g[r+1][c+1]=='M')
    cond2 = (g[r-1][c+1]=='M' and g[r+1][c-1]=='S') or (g[r-1][c+1]=='S' and g[r+1][c-1]=='M')

    if not (cond1 and cond2):
        return False
    
    return True
    

def main():
    input_lines = get_input_lines()

    total = 0
    for r in range(len(input_lines)):
        for c in range(len(input_lines[0])):
            total += is_x_mas(input_lines, (r, c))

    print(total)


if __name__=='__main__':
    main()