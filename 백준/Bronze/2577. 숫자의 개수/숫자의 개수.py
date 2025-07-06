A = int(input())
B = int(input())
C = int(input())

multiply = str(A*B*C)

for i in range(10):
    print(multiply.count(str(i)))