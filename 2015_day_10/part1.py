from itertools import groupby


def look_and_say(num:str)->str:
    r = [str(k)+str(len(list(g))) for k, g in groupby(num)]
    return ''.join(r)


def main():
    input_num = '1'
    for _ in range(4):
        input_num = look_and_say(input_num)
    print(input_num)

    input_num = '1113122113'
    for _ in range(40):
        input_num = look_and_say(input_num)
    print(len(input_num))

if __name__=='__main__':
    main()