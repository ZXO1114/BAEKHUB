n = int(input())


for i in range(n):
    cnt = 0
    score = 0
    OX_list = input()
    for ii in range(len(OX_list)):
        if OX_list[ii] == 'O':
            score += 1+cnt
            cnt += 1
        else:
            cnt = 0
    print(score)
