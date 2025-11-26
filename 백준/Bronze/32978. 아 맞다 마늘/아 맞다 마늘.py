import sys
input = sys.stdin.readline

n = int(input())
d = set(map(str,input().strip().split()))
s = set(map(str,input().strip().split()))

print(*(d-s))