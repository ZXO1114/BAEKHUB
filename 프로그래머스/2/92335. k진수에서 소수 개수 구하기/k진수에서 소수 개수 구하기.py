def jinsu(num, q):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    
def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    s = jinsu(n,k).split('0')
    # print(s)
    for i in s:
        if i != '' and isPrime(int(i)):
            answer += 1
    
    return answer
