import sys
input = sys.stdin.read

data = input().strip().split('\n')[1:]
nick_set = set()
s = 0
for row in data:
    if row == "ENTER":
        s += len(nick_set)
        nick_set = set([])
    else:
        nick_set.add(row)
print(s + len(nick_set))