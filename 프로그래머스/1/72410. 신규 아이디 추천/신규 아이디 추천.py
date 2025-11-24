import re

def solution(new_id):
    answer = new_id.lower() #1단계
    answer = re.sub(r"[^a-z0-9\-_.]", '', answer) #2단계
    answer = '.'.join(word for word in answer.split('.') if word) #3,4단계
    if not answer: answer = 'a' #5단계
    answer = answer[:15] #6단계
    if answer[-1] == '.':
        answer = answer[:-1]
    while True:
        if len(answer) >= 3:
            break
        answer += answer[-1]
    return answer