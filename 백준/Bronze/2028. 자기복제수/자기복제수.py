n = int(input())

for i in range(n):
    h = input()
    match len(h):
        case 1 if h == str((int(h)**2) % 10):
            print('YES')
        case 2 if h == str((int(h)**2) % 100):
            print('YES')
        case 3 if h == str((int(h)**2) % 1000):
            print('YES')
        case _:
            print('NO')