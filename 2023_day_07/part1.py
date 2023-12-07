
c_list = 'AKQJT98765432'
r = {c: len(c_list)-i for i, c in enumerate(c_list)}

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def score_type(_card):

    card = str(_card[0])

    score = 0
    while card:
        c = card[0]
        old_count = len(card)
        card = card.replace(c, '')
        new_count = len(card)
        score += pow(3, old_count-new_count)
    
    
    return score

def is_greater(card2, card1):
    s1 = score_type(card1)
    s2 = score_type(card2)
    if s2 > s1:
        return True
    if s1 > s2:
        return False
    for c1, c2 in zip(card1[0], card2[0]):
        if r[c2] > r[c1]:
            return True
        if r[c2] < r[c1]:
            return False

def sort_card(card_list):
    swap_enc = True

    new_list = list(card_list)
    while swap_enc:
        swap_enc = False
        for i in range(len(new_list)-1):
            card1 = new_list[i]
            card2 = new_list[i+1]
            if is_greater(card2, card1):
                swap_enc = True
                new_list[i] = card2
                new_list[i+1] = card1
    
    return new_list

def main():
    input_lines = get_input_lines()
    cards = []
    for line in input_lines:
        c, b = line.split()
        cards.append((c, int(b)))

    total = 0
    for i, card in enumerate(sort_card(cards)):
        total+=(len(cards)-i)*card[1]
    
    print(total)


if __name__=='__main__':
    main()