import math
T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    if (N % H) == 0:
        cus_H = H
    else:
        cus_H = N % H

    if int(math.ceil(N/H)) // 10 == 0:
        print(f"{cus_H}0{int(math.ceil(N/H))}")
    else:
        print(f"{cus_H}{int(math.ceil(N / H))}")