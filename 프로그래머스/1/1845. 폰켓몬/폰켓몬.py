def solution(nums):
    l = len(nums)//2
    type_max = len(set(nums)) 
    if type_max < l:
        answer = type_max
    else:
        answer = l
    return answer