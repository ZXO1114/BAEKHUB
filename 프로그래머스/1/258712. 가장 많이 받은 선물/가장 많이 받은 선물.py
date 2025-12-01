'''
return 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수
friends gifts answer present_list friends_dict
1. friends의 길이를 이용해 present_list만들기, friends_dict 만들기
2. gifts for문 돌려서 present_list 수정
3. present_list로 가장 많이 받는 친구의 선물수 구하기
'''
def solution(friends, gifts):
    l = len(friends)
    answer = [0] * l
    up_down_list = [0] * l
    present_list = [[0] * l for _ in range(l)]
    # print(present_list)
    friends_dict = {value:index for index, value in enumerate(friends)}
    # print(friends_dict)
    
    for gift in gifts:
        giver, reciever = gift.split()
        present_list[friends_dict[giver]][friends_dict[reciever]] += 1
    print(present_list)
    
    for friend in friends:
        down = 0
        for i in range(l):
            down += present_list[i][friends_dict[friend]]
        up_down_list[friends_dict[friend]] += sum(present_list[friends_dict[friend]]) - down
    print(up_down_list)
    
    for i in range(l-1):
        for j in range(i+1,l):
            if present_list[i][j] > present_list[j][i]:
                answer[i] += 1
            elif present_list[i][j] < present_list[j][i]:
                answer[j] += 1
            else:
                if up_down_list[i] > up_down_list[j]:
                    answer[i] += 1
                elif up_down_list[i] < up_down_list[j]:
                    answer[j] += 1
    return max(answer)