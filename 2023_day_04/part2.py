
def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():
    input_lines = get_input_lines()

    card_winning_count = {}
    card_count = {}

    for i, line in enumerate(input_lines):
        wl, ah = line.split(':')[-1].split('|')
        wl = wl.split()
        ah = ah.split()
        winning_count = 0
        for a in ah:
            if a in wl:
                winning_count += 1
        card_winning_count[i+1] = winning_count
        card_count[i+1] = 1

    for id, wc in card_winning_count.items():
        total_win = 0
        for _ in range(card_count[id]):
            for j in range(wc):
                index = id + j + 1
                card_count[index] += 1
                total_win += 1
        if total_win == 0:
            break
    
    print(sum([x for x in card_count.values()]))
    
if __name__=='__main__':
    main()