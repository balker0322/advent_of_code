import re

def main():
    ra, rb, rc, *ops = [int(x) for x in re.findall(r'\d+', open(0).read())]
    print(ra, rb, rc, ops)

    def get_next(ops, ip):
        return ops[ip], ip+1
    
    def comb_operand(val):
        if val==0: return 0
        if val==1: return 1
        if val==2: return 2
        if val==3: return 3
        if val==4: return ra
        if val==5: return rb
        if val==6: return rc

    output_list = []
    ip = 0
    while ip<len(ops):
        opcode, ip = get_next(ops, ip)
        operand, ip = get_next(ops, ip)

        if opcode==0:
            ra = int(ra/(2**comb_operand(operand)))
            continue
        
        if opcode==1:
            rb^=operand
            continue

        if opcode==2:
            rb = comb_operand(operand)%8

        if opcode==3:
            if ra!= 0: ip = operand
            continue

        if opcode==4:
            rb^=rc
            continue

        if opcode==5:
            output_list.append(comb_operand(operand)%8)
            continue

        if opcode==6:
            rb = int(ra/(2**comb_operand(operand)))
            continue

        if opcode==7:
            rc = int(ra/(2**comb_operand(operand)))
            continue
    # print(output_list)
    print(','.join([str(n) for n in output_list]))


if __name__=='__main__':
    main()