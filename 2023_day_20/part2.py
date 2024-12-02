from collections import deque

def get_input_lines():
    return [line.strip() for line in open(0).readlines()]

def print_inv(label, sig_dict, tabs=''):
    print(tabs, label)
    if 'broadcaster' in sig_dict[label]:
    # if label=='broadcaster':
        return
    for d in sig_dict[label]:
        print_inv(d, sig_dict, tabs+' ')


def main():

    input_lines = get_input_lines()
    signals = {}

    sig_state = {}
    sig_set = set([])

    for line in input_lines:
        src, dest = line.split(' -> ')
        dest = dest.split(', ')

        sig_set.add(src)
        for d in dest:
            sig_set.add(d)

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
            'input_list':[],
        }
        sig_state[src] = 'LO'


    for key, val in signals.items():
        for dest in val['dest']:
            if not dest in signals.keys():
                continue
            if signals[dest]['src_type'] == '&':
                signals[dest]['state'][key] = 'LO'
                signals[dest]['input_list'].append(key)


    # q = deque([])
    # q.appendleft(('rx', None))

    inv_signal = {}

    for key in list(signals.keys()) + ['rx']:
        src = []
        for __key, __val in signals.items():
            if key in __val['dest']:
                src.append(__key)
        inv_signal[key] = src
        if key not in signals.keys():
            continue

    for key, src in inv_signal.items():
        if key not in signals.keys():
            continue
        print(signals[key]['src_type']+key, [signals[s]['src_type']+s for s in src])
        for __key in src:
            print(' -> ' ,signals[__key]['src_type']+__key, [signals[s]['src_type']+s for s in inv_signal[__key]])


    # # print_inv('rx', inv_signal)
    exit()

    lo_count = 0
    hi_count = 0

    button_cnt = 0

    states = set([])
    # states.add(tuple([sig_state[k] for k, v in signals.items() if v['src_type'] == '&']))

    unchanged_nodes = set([s for s in sig_state.keys()])
    changed_nodes_group = set([])

    
    old_sig_state = dict(sig_state)

    state_disp = {s:[v] for s, v in sig_state.items()}
            
    def run_single_sim(intial_sig_state):
        sig_state = dict(intial_sig_state)
        q = deque([])
        q.appendleft(('LO', 'broadcaster', 'button'))

        while q:
            in_pulse, curr, src = q.pop()

            if not curr in signals.keys():
                # print(in_pulse)
                if in_pulse=='LO':
                    print(button_cnt, curr, in_pulse)
                    exit()
                continue

            if signals[curr]['src_type'] in ['button', 'broadcaster']:
                out_pulse = in_pulse
            
            if signals[curr]['src_type']=='%':
                if in_pulse=='LO':
                    if sig_state[curr]=='LO':
                        sig_state[curr] = 'HI'
                    else:
                        sig_state[curr] = 'LO'
                    out_pulse = sig_state[curr]
                else:
                    continue

            if signals[curr]['src_type']=='&':
                sig_state[src]=in_pulse
                if all([sig_state[v]=='HI' for v in signals[curr]['input_list']]):
                    out_pulse = 'LO'
                else:
                    out_pulse = 'HI'

            sig_state[curr] = out_pulse

            for d in signals[curr]['dest']:
                q.appendleft((out_pulse, d, curr))
            
        return sig_state

    

    def run_sim(__sig_state, max_button_cnt):

        sig_state = dict(__sig_state)
        old_sig_state = dict(__sig_state)
        period_counter = {s:[0, False, False] for s, _ in sig_state.items()}

        button_cnt = 0
        
        # for bi in range(max_button_cnt):

        #     button_cnt = bi+1
        while True:
            button_cnt+=1

            disp=False
            for k, v in period_counter.items():
                cnt, rise_enc_1, rise_enc_2 = v
                if rise_enc_2==False and rise_enc_1==True and old_sig_state[k]=='LO' and sig_state[k]=='HI':
                    period_counter[k][2]=True
                    # print(k, period_counter[k][0])
                    disp = True
                if rise_enc_2==False and old_sig_state[k]=='LO' and sig_state[k]=='HI':
                    period_counter[k][1]=True
                if period_counter[k][1]==True and period_counter[k][2]==False:
                    period_counter[k][0] += 1

                
                # if rise_enc_2==False and rise_enc_1==True and old_sig_state[k]=='LO' and sig_state[k]=='HI':
                #     period_counter[k][2]=True
                #     # print(k, period_counter[k][0])
                #     disp = True
                # if rise_enc_2==False and old_sig_state[k]=='LO' and sig_state[k]=='HI':
                #     period_counter[k][1]=True
                # if period_counter[k][1]==True and period_counter[k][2]==False:
                #     period_counter[k][0] += 1

            if disp:  
                for k, v in period_counter.items():
                    # if period_counter[k][2]:
                    if period_counter[k][2]:
                        print(k, period_counter[k][0])
                    else:
                        print(k, sig_state[k], 'not done')
                        continue
                print(button_cnt)
                print('======================')
                        
            old_sig_state = dict(sig_state)

            sig_state = run_single_sim(sig_state)
            
        return sig_state
    
    sig_state = {s:'LO' for s in sig_set}

    # button_cnt = 0
    # mem = set([])
    # while True:
    #     button_cnt += 1
    #     sig_state = run_single_sim(sig_state)
    #     mem.add(tuple([v for k, v in sig_state.items()]))
    #     print(button_cnt, len(mem))


    sig_state = run_sim(sig_state, 4096)
    for k, v in sig_state.items():
        if k=='broadcaster':
            continue
        print(k, v)

    print(lo_count*hi_count)

if __name__=='__main__':
    main()