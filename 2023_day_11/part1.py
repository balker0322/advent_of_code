from itertools import combinations

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def traverse_graph(g):
    new_g = [[None for _ in range(len(g))] for _ in range(len(g[0]))]
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            new_g[c][r] = col
    return new_g

def expand_u(u):
    u = list(u)
    new_u = []
    for row in u:
        new_u.append(row)
        if all([i=='.' for i in row]):
            new_u.append(row)
    u = list(new_u)
    u = traverse_graph(u)
    new_u = []
    for row in u:
        new_u.append(row)
        if all([i=='.' for i in row]):
            new_u.append(row)
    u = traverse_graph(new_u)
    return u


def main():
    input_lines = get_input_lines()
    u = []
    for line in input_lines:
        row = []
        for c in line:
            row.append(c)
        u.append(row)

    u = expand_u(u)
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
        d = abs(ra-rb) + abs(ca-cb)
        total += d

    print(total)
    


if __name__=='__main__':
    main()