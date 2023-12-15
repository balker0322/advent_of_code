
from collections import deque 

def hash(x:str):
    val = 0
    for c in x:
        val+=ord(c)
        val*=17
        val%=256
    return val

class Box:

    def __init__(self):
        self.__box = {}

    def add(self, label, fl):

        box_num = hash(label)

        if not box_num in self.__box.keys():
            self.__box[box_num] = [(label, fl)]
            return

        temp_box = []
        label_is_existing = False
        while self.__box[box_num]:
            c_label, c_fl = self.__box[box_num].pop()
            if c_label==label:
                temp_box.append((c_label, fl))
                label_is_existing = True
                break
            temp_box.append((c_label, c_fl))

        while temp_box:
            c_label, c_fl = temp_box.pop()
            self.__box[box_num].append((c_label, c_fl))
        
        if not label_is_existing:
            self.__box[box_num].append((label, fl))

    def remove(self, label):
        box_num = hash(label)

        if not box_num in self.__box.keys():
            return

        temp_box = []

        while self.__box[box_num]:
            c_label, c_fl = self.__box[box_num].pop()
            if c_label==label:
                continue
            temp_box.append((c_label, c_fl))

        while temp_box:
            c_label, c_fl = temp_box.pop()
            self.__box[box_num].append((c_label, c_fl))
    
    def get_power(self):
        total = 0
        for key, val in self.__box.items():
            a = key+1
            for i, v in enumerate(val):
                _, fl = v
                b = i+1
                c = fl
                total += (a*b*c)
        return total
    
    def print_box(self):
        return
        for key, val in self.__box.items():
            print('box', key, ': ', val)
        print()


def main():
    inp = open(0).read().replace('\n', '').split(',')
    result = sum([hash(i.split('=')[0].split('-')[0]) for i in inp])

    box = Box()

    box.print_box()
    
    for item in inp:

        if '=' in item:
            label, fl = item.split('=')
            fl = int(fl)
            box.add(label, fl)
            box.print_box()
            continue

        if '-' in item:
            label = item.split('-')[0]
            box.remove(label)
            box.print_box()
            continue
    
    print(box.get_power())

if __name__=='__main__':
    main()