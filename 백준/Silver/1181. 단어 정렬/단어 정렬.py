n = int(input())
l = [input() for _ in range(n)]


l = list(set(l))


l.sort(key = lambda x: (len(x), x))

for word in l:
    print(word)