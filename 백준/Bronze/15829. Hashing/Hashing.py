n = int(input())
r = 31
M = 1234567891
i_str = input()
result = 0

for i in range(n):
    result += ((ord(i_str[i])-96) * (r**i))

print(result % M)