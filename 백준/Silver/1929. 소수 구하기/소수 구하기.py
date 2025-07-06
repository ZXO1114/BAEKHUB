def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False

    for k in range(3, int(num**0.5) + 1, 2):
        if num % k == 0:
            return False
    return True

import sys
n,m = map(int,sys.stdin.readline().split())

for i in range(n,m+1):
    if is_prime(i):print(i)