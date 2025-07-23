n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list = list(sorted(num_list))
for item in num_list:
    print(item)