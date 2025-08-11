n = input()
n_sum = 0
for i in n:
    if i == '0':
        n_sum += 9
    else:
        n_sum += int(i)
print(n_sum)