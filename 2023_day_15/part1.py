

def hash(x:str):
    val = 0
    for c in x:
        val+=ord(c)
        val*=17
        val%=256
    return val

def main():
    inp = open(0).read().replace('\n', '').split(',')
    result = sum([hash(i) for i in inp])
    print(result)

if __name__=='__main__':
    main()