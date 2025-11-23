'''
return 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태
numbers left_hand right_hand left_distance right_distance hand answer
1 2 3
4 5 6
7 8 9
* 0 #
1,4,7은 무조건 왼손 3,6,9는 오른손
거리가 같을시 hand에 따라서
시작은 * #에서
* = 10, 0 = 11, # = 12로 생각
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
거리공식
2,5,8,11(0)에서 손까지 떨어진 거리(number - (left_hand or right_hand)) 별 칸수
|1|, |3|은 1칸 (상하좌우)
|2|, |4|, |6|은 2칸 (한칸 위 아래 대각선 숫자들, 2칸 상하)
|5|, |7|, |9|은 3칸 (두칸 위 아래 대각선 숫자들, 3칸 상하)
|8|, |10|은 4칸 (3칸 위 아래 대각선 숫자들)

1. for 문으로 numbers 요소들 하나씩 얻기
2. number가 1,4,7 이면 answer += 'L' 3,6,9 면 answer += 'R'하고 left_hand 또는 right_hand 변경
3. 둘 다 아닐시 left_distance = n - left_hand, right_distance = n - right_distance
4.  if 문으로 실제 거리로 변경
5. 더 짧은 거리를 가지고 있는 손 answer 문자열에 더하고 left_hand or right_hand 변경
6. 거리가 같을시 hand를 따라서
'''

def solution(numbers, hand):
    answer = ''
    left_hand, right_hand = 10, 12 
    # print(left_hand, right_hand)
    left_distance, right_distance = 0, 0
    # print(left_distance, right_distance)
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left_hand = number
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            right_hand = number
            answer += 'R'
        else:
            if number == 0: number = 11
            left_distance = abs(number - left_hand)
            right_distance = abs(number - right_hand)
            
            if left_distance == 1 or left_distance == 3: left_distance = 1
            elif left_distance == 2 or left_distance == 4 or left_distance == 6: left_distance = 2
            elif left_distance == 5 or left_distance == 7 or left_distance == 9: left_distance = 3
            elif left_distance == 8 or left_distance == 10: left_distance = 4
            
            if right_distance == 1 or right_distance == 3: right_distance = 1
            elif right_distance == 2 or right_distance == 4 or right_distance == 6: right_distance = 2
            elif right_distance == 5 or right_distance == 7 or right_distance == 9: right_distance = 3
            elif right_distance == 8 or right_distance == 10: right_distance = 4
                
            if left_distance == right_distance:
                if hand == "left":
                    left_hand = number
                    answer += 'L'
                else:
                    right_hand = number
                    answer += 'R'
            elif left_distance < right_distance:
                left_hand = number
                answer += 'L'
            else:                    
                right_hand = number
                answer += 'R'
    return answer