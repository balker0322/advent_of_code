from itertools import combinations

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def traverse_graph(g):
    new_g = [[None for _ in range(len(g))] for _ in range(len(g[0]))]
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            new_g[c][r] = col
    return new_g

def expand_u(u, age=2):
    u = list(u)
    new_u = []
    for row in u:
        new_u.append(row)
        if all([i=='.' for i in row]):
            for _ in range(age-1):
                new_u.append(row)
    u = list(new_u)
    u = traverse_graph(u)
    new_u = []
    for row in u:
        new_u.append(row)
        if all([i=='.' for i in row]):
            for _ in range(age-1):
                new_u.append(row)
    u = traverse_graph(new_u)
    return u

age = 1_000_000

def main():
    input_lines = get_input_lines()
    u = []
    for line in input_lines:
        row = []
        for c in line:
            row.append(c)
        u.append(row)

    empty_row_index = set([])
    empty_col_index = set([])
    
    for r, row in enumerate(u):
        if all([i=='.' for i in row]):
            empty_row_index.add(r)
    
    for c in range(len(u[0])):
        if all([row[c]=='.' for row in u]):
            empty_col_index.add(c)

    galaxies = []
    for r, row in enumerate(u):
        for c, col in enumerate(row):
            if col=='#':
                galaxies.append((r, c))
    total = 0
    for pair in combinations(galaxies, 2):
        ga, gb = pair
        ra, ca = ga
        rb, cb = gb

        min_r, max_r = sorted([ra, rb])
        min_c, max_c = sorted([ca, cb])
        covered_r = set([i for i in range(min_r, max_r+1)])
        covered_c = set([i for i in range(min_c, max_c+1)])

        covered_empty_r = covered_r.intersection(empty_row_index)
        covered_empty_c = covered_c.intersection(empty_col_index)

        d = abs(ra-rb) + abs(ca-cb) + (len(covered_empty_r) + len(covered_empty_c))*(age-1)
        total += d

    print(total)
    


if __name__=='__main__':
    main()