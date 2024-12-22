
def main():
    patterns, designs = open(0).read().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.split('\n')
    cache = {}

    def get_possible_comb(d:str):
        if d=='': return 1
        if d in cache: return cache[d]
        total = 0
        for pat in patterns:
            if not d.startswith(pat):
                continue
            total += get_possible_comb(d[len(pat):])
        cache[d]=total
        return total
    
    print(sum(get_possible_comb(d) for d in designs))

if __name__=='__main__':
    main()