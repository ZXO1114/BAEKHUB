for _ in range(3):
    n_sum = 0
    for i in range(int(input())):
        n_sum += int(input())
    if n_sum > 0:
        print('+')
    elif n_sum == 0:
        print(0)
    else:
        print('-')