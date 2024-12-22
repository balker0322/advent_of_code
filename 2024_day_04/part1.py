
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def get_xmas_count(g, origin_coor, dir_coor, found_word):
    
    if found_word=='XMAS':
        return True
    
    r, c = origin_coor
    dr, dc = dir_coor

    if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]):
        return False

    new_coor = (r+dr, c+dc)
    new_found_word = found_word+g[r][c]
    
    if 'XMAS'.startswith(new_found_word):
        return get_xmas_count(g, new_coor, dir_coor, new_found_word)

    return False

def main():
    input_lines = get_input_lines()

    total = 0
    for r in range(len(input_lines)):
        for c in range(len(input_lines[0])):
            total += get_xmas_count(input_lines, (r, c), (0, 1), '')
            total += get_xmas_count(input_lines, (r, c), (0, -1), '')
            total += get_xmas_count(input_lines, (r, c), (1, 1), '')
            total += get_xmas_count(input_lines, (r, c), (1, -1), '')
            total += get_xmas_count(input_lines, (r, c), (1, 0), '')
            total += get_xmas_count(input_lines, (r, c), (-1, 1), '')
            total += get_xmas_count(input_lines, (r, c), (-1, -1), '')
            total += get_xmas_count(input_lines, (r, c), (-1, 0), '')

    print(total)


if __name__=='__main__':
    main()