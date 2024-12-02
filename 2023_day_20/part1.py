from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def main():

    input_lines = get_input_lines()
    signals = {}

    for line in input_lines:
        src, dest = line.split(' -> ')
        dest = dest.split(', ')
        if src=='broadcaster':
            src_type, src = src, src
            state = None
        else:
            src_type, src = src[0], src[1:]
            if src_type=='%':
                state = 'LO'
            if src_type=='&':
                state = {}
        signals[src] = {
            'src_type':src_type,
            'dest':dest,
            'state':state,
        }


    for key, val in signals.items():
        for dest in val['dest']:
            if not dest in signals.keys():
                continue
            if signals[dest]['src_type'] == '&':
                signals[dest]['state'][key] = 'LO'

    lo_count = 0
    hi_count = 0

    for _ in range(1000):
        
        q = deque([])
        q.appendleft(('LO', 'broadcaster', 'button'))
        while q:
            in_pulse, curr, src = q.pop()

            if in_pulse=='LO':
                lo_count += 1
            if in_pulse=='HI':
                hi_count += 1

            # print(src, in_pulse, '->', curr)

            if not curr in signals.keys():
                continue

            if signals[curr]['src_type'] in ['button', 'broadcaster']:
                out_pulse = in_pulse
            
            if signals[curr]['src_type']=='%':
                if in_pulse=='LO':
                    if signals[curr]['state']=='LO':
                        signals[curr]['state'] = 'HI'
                    else:
                        signals[curr]['state'] = 'LO'
                    out_pulse = signals[curr]['state']
                else:
                    continue

            if signals[curr]['src_type']=='&':
                signals[curr]['state'][src]=in_pulse
                if all([v=='HI' for v in signals[curr]['state'].values()]):
                    out_pulse = 'LO'
                else:
                    out_pulse = 'HI'

            for d in signals[curr]['dest']:
                q.appendleft((out_pulse, d, curr))


    print(lo_count*hi_count)

if __name__=='__main__':
    main()