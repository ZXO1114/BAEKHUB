def solution(s):
    cnt_dict = {}
    
    replace_word = ["{","}",","]
    for word in replace_word:
        s = s.replace(word," ")
        
    # print(s)
    num_list = list(map(int,s.split()))
    # print(num_list)
    
    l = len(set(num_list))
    answer = [0] * l
    
    for num in num_list:
        if num not in cnt_dict:
            cnt_dict[num] = 1
        else:
            cnt_dict[num] += 1
    # print(cnt_dict)
    
    for num, value in cnt_dict.items():
        answer[-value] = num
        
    # print(answer)
    
    return answer