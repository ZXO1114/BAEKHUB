import math
n = int(input())
files = list(map(int,input().split()))
c = int(input())
files = [math.ceil(file/c) for file in files]
print(sum(files)*c)