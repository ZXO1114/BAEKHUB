o, w = map(int,input().split())
i = 1
while o != 0 and w != 0:
    d = 0
    b, n = map(str,input().split())
    n = int(n)
    while b != '#':
        if b == 'E':
            w -= n
            if w <= 0:
                d = 1
        elif b =='F':
            w += n
        b, n = map(str, input().split())
        n = int(n)
    print(i,end=' ')
    i += 1
    if d == 0:
        if o/2 < w <o*2:
            print(':-)')
        else:
            print(':-(')
    else:
        print("RIP")
    o, w = map(int,input().split())
