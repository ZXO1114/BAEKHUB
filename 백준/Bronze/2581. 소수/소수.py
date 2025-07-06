def is_prime(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

M = int(input())
N = int(input())
sum = 0
min = 0

for i in range(M,N+1):
    if is_prime(i):
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)