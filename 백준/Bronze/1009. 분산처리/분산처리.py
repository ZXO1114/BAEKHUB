import sys
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    a %= 10

    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 0:
        print(10)
    elif a == 4 or a == 9:
        if b % 2 == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)