def solution(participant, completion):
    answer = ''
    participant_dict = {}
    for p in participant:
        if p not in participant_dict:
            participant_dict[p] = 1
        else:
            participant_dict[p] += 1
    # print(participant_dict)
    
    for c in completion:
        participant_dict[c] -= 1
    
    for key,value in participant_dict.items():
        if value >= 1:
            answer += key
    
    return answer