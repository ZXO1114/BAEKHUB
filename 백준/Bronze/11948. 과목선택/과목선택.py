s_list = []
h_list = []
for i in range(4):
    s_list.append(int(input()))
s_list.sort()
for i in range(2):
    h_list.append(int(input()))
h_list.sort()
print(s_list[-1]+s_list[-2]+s_list[-3]+h_list[-1])
