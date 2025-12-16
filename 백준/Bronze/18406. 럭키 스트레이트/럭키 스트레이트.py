import sys
input = sys.stdin.readline

st = input().strip()
l, r = st[:len(st)//2], st[len(st)//2:]
if sum([int(num) for num in l]) == sum([int(num) for num in r]):
    print("LUCKY")
else:
    print("READY")