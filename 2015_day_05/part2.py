
def cond1(s):
    for i in range(len(s)-1):
        tlp = s[i:i+2]
        if tlp in s[i+2:]:
            return True
    return False

def cond2(s):
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            return True
    return False

def is_nice(s):
    if not cond1(s):
        return False
    if not cond2(s):
        return False
    return True

def main():
    input_list = None
    with open(r'2015_day_05\input.txt', 'r') as f:
        input_list = [line.strip() for line in f.readlines()]
    
    ans = len([s for s in input_list if is_nice(s)])
    print(ans)

if __name__=='__main__':
    main()