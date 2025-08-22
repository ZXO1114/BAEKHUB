s_l = [0,0]
for i in range(int(input())):
    if input() == 'D':
        s_l[0] += 1
    else:
        s_l[1] += 1
    if (s_l[0]-s_l[1]) == 2 or (s_l[1]-s_l[0]) == 2: break
print(f'{s_l[0]}:{s_l[1]}')