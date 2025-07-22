input_list = list(map(int,input().split()))
sorted_list = list(sorted(input_list))

sum_ot = sorted_list[0] + sorted_list[1]

if sorted_list[2] >= sum_ot:
    sum_ot = (sum_ot * 2) -1
else:
    sum_ot += sorted_list[2]
print(sum_ot)