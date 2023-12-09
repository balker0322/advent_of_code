

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()
    hist_list = [list(map(int, l.split())) for l in input_lines]
    
    total = 0
    for h in hist_list:
        nh = list(h)
        to_add = True
        while True:
            if to_add:
                total += nh[0]
            else:
                total -= nh[0]
            to_add = not to_add
            nh = [nh[i+1]-nh[i] for i in range(len(nh)-1)]
            if sum(nh)==0:
                break
            
    print(total)

if __name__=='__main__':
    main()