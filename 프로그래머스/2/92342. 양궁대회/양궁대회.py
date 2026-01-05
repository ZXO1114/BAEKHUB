def solution(n, info):
    cost_list = [(info[i]+1,10-i) for i in range(11)]
    answer = [[-1]] #1
    # print(cost_list)
    for idx in range(1,1025): #2
        bin_idx = bin(idx)[2:] #3
        bin_idx = bin_idx.zfill(10) #4
        # print(bin_idx)
        c = list_check(bin_idx,info,cost_list,n)
        if c != False:
            answer = change_check(c,answer)
        
    return answer[-1]

def list_check(BIN_IDX,apeach_list,COST_LIST,n):
    lions_list = []
    lions_score = 0
    apeach_score = 0
    for bit_idx, bit in enumerate(BIN_IDX):    
        # print(bit_idx,bit)
        if bit == '1':
            lions_list.append(COST_LIST[bit_idx][0])
            n -= COST_LIST[bit_idx][0]
            lions_score += COST_LIST[bit_idx][1]
            if n < 0:
                return False
        else:
            if apeach_list[bit_idx] != 0:
                apeach_score += COST_LIST[bit_idx][1]
            lions_list.append(0)
    if (lions_score - apeach_score) <= 0:
        return False
    lions_list += [n]
    return lions_score - apeach_score, lions_list

def change_check(SCORE_LIONS_LIST,ANSWER):
    if ANSWER == [[-1]] or SCORE_LIONS_LIST[0] > ANSWER[0]:
        return SCORE_LIONS_LIST
    elif SCORE_LIONS_LIST[0] < ANSWER[0]:
        return ANSWER
    else:
        if up_down_check(-1, SCORE_LIONS_LIST[1], ANSWER[1]):
            return SCORE_LIONS_LIST
        else:
            return ANSWER
    
def up_down_check(udidx, list1, list2):
    if list1[udidx] > list2[udidx]:
        return True
    elif list1[udidx] < list2[udidx]:
        return False
    else:
        return up_down_check(udidx-1, list1, list2)
    
    