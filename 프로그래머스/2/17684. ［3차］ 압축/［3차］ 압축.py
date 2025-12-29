def solution(msg):
    answer = []
    dictionary = {chr(64+value):value for value in range(1,27)}
    # print(dictionary)
    msg_size = len(msg)
    dictionary_size = 27
    l = 0
    while l < msg_size:
        i = 1
        while l+(i+1) <= msg_size and msg[l:l+(i+1)] in dictionary:
            i += 1
        answer.append(dictionary[msg[l:l+i]])
        dictionary[msg[l:l+(i+1)]] = dictionary_size
        dictionary_size += 1
        l += i
            
    return answer