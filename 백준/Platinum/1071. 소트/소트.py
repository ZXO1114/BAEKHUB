import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().strip().split()))
num_list.sort()
# print(num_list)
# print(len(set(num_list)))
# print(num_list[0] == num_list[-1] -1)
answer = [1001]
while num_list:
    if len(set(num_list)) == 2 and num_list[0] == num_list[-1] -1:
        # print('fff')
        for _ in range(len(num_list)):
            answer.append(num_list.pop())
    for i,num in enumerate(num_list):
        if num != answer[-1] + 1:
            answer.append(num)
            # print(f"--{num}--")
            del num_list[i]
            break

print(*answer[1:])