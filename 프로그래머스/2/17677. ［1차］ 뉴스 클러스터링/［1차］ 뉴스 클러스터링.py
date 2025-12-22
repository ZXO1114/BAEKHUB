'''
return 두 문자열의 자카드 유사도
str1 str2 answer one_list two_list inter_num
자카드 유사도 = 다중집합의 교집합의 원소의 개수 / 합집합 원소의 개수 = 다중집합의 교집합의 원소의 개수 / 두 리스트의 길이 max
@@@@ 대문자와 소문자의 차이는 무시한다
@@@집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
1. str1의 리스트로 만든다
2. str2도 만든다
3. set(one_list)를 for으로 돌린다
4. inter_num += min(one_list.count(letter), two_list.count(letter))
5. 자크드 유사도를 구하고 65536을 곱하후 소수점을 버린다
'''

import re

def solution(str1, str2):
    answer = 0
    inter_num = 0
    union_num = 0
    str1 = re.sub(r"[^a-z]", '*', str1.lower())
    str2 = re.sub(r"[^a-z]", '*', str2.lower())
    # print(str1)
    # print(str2)
    one_list = [str1[i] + str1[i+1] for i in range(len(str1)-1) if '*' not in (str1[i] + str1[i+1])]
    two_list = [str2[i] + str2[i+1] for i in range(len(str2)-1) if '*' not in (str2[i] + str2[i+1])]
    print(one_list)
    print(two_list)
    
    for letter in (set(one_list) | set(two_list)):
        inter_num += min(one_list.count(letter), two_list.count(letter))
        union_num += max(one_list.count(letter), two_list.count(letter))
            
    print(inter_num)
    print(union_num)
    
    if union_num == 0:
        answer = 65536
    elif inter_num == 0:
        answer = 0
    else:
        answer = int((inter_num/union_num)*65536)
    return answer