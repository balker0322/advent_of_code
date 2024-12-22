import re
from collections import deque

def get_next(ops, ip):
    return ops[ip], ip+1

def comb_operand(val, ra, rb, rc):
    if val==0: return 0
    if val==1: return 1
    if val==2: return 2
    if val==3: return 3
    if val==4: return ra
    if val==5: return rb
    if val==6: return rc

def run(ra, rb, rc, *ops):
    ra, rb, rc = int(ra), int(rb), int(rc)
    output_list = []
    ip = 0
    while ip<len(ops):
        opcode, ip = get_next(ops, ip)
        operand, ip = get_next(ops, ip)
        co = comb_operand(operand, ra, rb, rc)

        if opcode==0: ra = int(ra/(2**co))
        if opcode==1: rb^=operand
        if opcode==2: rb = co%8
        if opcode==3 and ra!= 0: ip = operand
        if opcode==4: rb^=rc
        if opcode==5: output_list.append(co%8)
        if opcode==6: rb = int(ra/(2**co))
        if opcode==7: rc = int(ra/(2**co))  

    return tuple(output_list)

def run2(ra, rb, rc, *ops):
    a, b, c = ra, rb, rc
    output_list = []

    while True:
        b=a%8
        b=b^7
        c=a>>b
        a=a>>3
        b=b^7
        b=b^c
        output_list.append(b%8)
        if a==0:
            break
    return tuple(output_list)

def find_solution(ops, ans):
    if ops==[]: return ans
    # output_list = []
    for b in range(8):
        a = ans << 3
        a = (a | b)
        # b=a%8
        b=b^7
        c=a>>b
        # a=a>>3
        b=b^7
        b=b^c
        if b%8==ops[-1]:
            s = find_solution(ops[:-1], a)
            if s: return s
            continue
        # output_list.append(b%8)
    return None

def find_min_solution(a, b, c, d):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd, x, y = extended_gcd(b, d)
    if (c - a) % gcd != 0:
        return None  # No solution

    k = (c - a) // gcd
    m = k * x
    n = -k * y

    # Ensure m and n are positive
    while m <= 0 or n <= 0:
        m += d // gcd
        n += b // gcd
    return m, n

# def get_comm(a, da, b, ba):
#     if a==b:
#         return a

def main():
    ra, rb, rc, *ops = [int(x) for x in re.findall(r'\d+', open(0).read())]
    # ops = tuple(ops)
    print(find_solution(ops, 0))
    exit()
    # print(run2(117440, rb, rc, *ops));
    # exit()

    i=0
    m = set({})
    ss = ''
    while True:
        s = ''
        for ii in range(2**3):
            # print(ii, i+ii, run(i+ii, rb, rc, *ops))
            s+=str(run(i+ii, rb, rc, *ops)[0])
        if s in m:
            break
        m.add(s)
        ss+=s
        i+=8
    
    # print(ss); exit()

    possible_index = {}
    for i, op_num in enumerate(ops):
        possible_index[i] = []
        for ii, s in enumerate(ss):
            if i==len(ops)-1 and ii==0:
                continue
            if int(s)==op_num:
                # for iii in range(8):
                possible_index[i].append(ii)
        # print(ops[i], possible_index[i])

    print(possible_index)
    remaining_set = None
    for i in range(len(ops)):
        j = len(ops)-i-1
        if remaining_set is None:
            remaining_set = set(possible_index[j])
            continue
        # print(remaining_set)
        curr_set = set(possible_index[j])
        new_set = set([])
        for n in remaining_set:
            for ni in range(8):
                new_set.add((n*8)+ni)

        # lenss = len(ss)
        # remaining_set = set([])
        # visited = set([])
        # for a in new_set:
        #     for b in curr_set:
        #         if (a, b) in visited:
        #             continue
        #         # a+b*m = c+d*n
        #         if a==b:
        #             remaining_set.add(a)
        #             continue
        #         ans = find_min_solution(a, 8*lenss, b, lenss)
        #         if ans:
        #             m, n = ans
        #             remaining_set.add(a+8*lenss*m)
        #             print(a, b, a+lenss*m)
        # print(remaining_set)
                
        additional_set = set([])
        x = max(1, int((max(new_set)-min(curr_set))/len(ss))-1)
        # print(x)
        for n in curr_set:
            additional_set.add((x*len(ss))+n)
        curr_set|=additional_set
        # print(curr_set, new_set)

        while True:
            remaining_set = curr_set&new_set
            if remaining_set:
                break

            additional_set = set([])
            for n in curr_set:
                additional_set.add((len(ss))+n)
            curr_set|=additional_set

        # print(j, len(ss))
        # print(new_set)
        # print(possible_index[j])
        # print(remaining_set)
        # print()
        
    print(min(remaining_set))

    exit()



    ops = list(ops)
    base_num = 8
    count = 0
    msb = True
    while ops:
        count *= base_num
        op_num = ops.pop()
        for i, s in enumerate(ss):
            if msb and i==0:
                msb = False
                continue
            if int(s)==op_num:
                print(op_num, i)
                count += (i%base_num)
                break
    
    print(count)

    # digit_index = {}

    # for i in range((2**3)*(2**3)):
    #     result = run(i, rb, rc, *ops)[0]
    #     if not result in digit_index:
    #         digit_index[result] = set([])
    #     digit_index[result].add(i%8)
    #     print(i%8, run(i, rb, rc, *ops))
    
    # print(digit_index)
    # exit()


    # q = deque([])
    # visited = set([])
    # l = len(ops)

    # for num in digit_index[ops[0]]:
    #     q.append(((num, ), 0))

    # while q:
    #     node = q.popleft()
    #     if node in visited:
    #         continue
        
    #     seq, i = node

    #     if i+1>=l:
    #         print(seq)
    #         continue
    #     # print(ops[i+1], digit_index)
    #     for num in digit_index[ops[i+1]]:
    #         q.append((seq+(num, ), i+1))

    #     visited.add(node)


    # bit_val = {i:run(i, rb, rc, *ops)[0] for i in range(2**3)}
    # print(digit_index)


    # print(bit_val)
    # ra=0
    # while True:
    #     output_list = run(ra, rb, rc, *ops)
    #     print(ra, ops, output_list)
    #     if ops==output_list:
    #         print(ra)
    #         exit()
    #     ra += 1
    #     if ra==4000: exit()

if __name__=='__main__':
    main()