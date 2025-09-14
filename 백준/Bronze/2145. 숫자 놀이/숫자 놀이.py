n = input()

while n != '0':
    while len(n) > 1:
        n = str(sum([int(i) for i in n]))
    print(n)
    n = input()
