from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def c(k, v):
    try:
        r = int(k)
        return r
    except:
        return v[k]

def parse(s, v):
    if 'AND' in s:
        k1, k2, key =  s.split()[::2]
        return key, c(k1, v)&c(k2, v)
    if 'OR' in s:
        k1, k2, key =  s.split()[::2]
        return key, c(k1, v)|c(k2, v)
    if 'LSHIFT' in s:
        k1, k2, key =  s.split()[::2]
        return key, c(k1, v)<<c(k2, v)
    if 'RSHIFT' in s:
        k1, k2, key =  s.split()[::2]
        return key, c(k1, v)>>c(k2, v)
    if 'NOT' in s:
        _, k1, _, key =  s.split()
        return key, ~c(k1, v)
    value, key = s.split()[::2]
    return key, c(value, v)

def convert_u16(value):
    if value < 0:
        return 65535 + value + 1
    return value

def main():
    input_lines = deque(get_input_lines())
    v = {}

    while input_lines:
        s = input_lines.pop()
        key = s.split()[-1]
        try:
            key, value = parse(s, v)
            v[key] = convert_u16(value)
            continue
        except:
            input_lines.appendleft(s)

    if 'a' in v.keys():
        print(v['a'])

if __name__=='__main__':
    main()