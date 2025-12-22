def jinsu(num, q):
    rev_base = ''
    
    if num == 0:
        return '0'
    
    while num > 0:
        num, mod = divmod(num, q)
        if q >= 10 and mod >= 10:
            c = 64 + (mod-9)
            rev_base += chr(c)
        else:
            rev_base += str(mod)

    return rev_base[::-1] 

def solution(n, t, m, p):
    answer = ''
    string_n = ''
    h = 0
    max_len = m*(t-1)+p
    
    while len(string_n) < max_len:
        string_n += jinsu(h,n)
        h += 1
    # print(string_n)
    
    for i in range(p-1, max_len, m):
        answer += string_n[i]
    return answer