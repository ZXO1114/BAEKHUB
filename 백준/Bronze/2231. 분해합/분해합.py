N = int(input())\

for i in range(N):
    check_sum = 0
    for ii in str(i):
        check_sum += int(ii)
    if i + check_sum == N:
        print(i)
        break
    elif i == N-1:
        print(0)
        break
