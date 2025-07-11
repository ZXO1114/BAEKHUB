x_list = []
y_list = []

result_x,result_y = 0,0

for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x),y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:
        result_x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        result_y = y_list[j]
print(result_x,result_y)