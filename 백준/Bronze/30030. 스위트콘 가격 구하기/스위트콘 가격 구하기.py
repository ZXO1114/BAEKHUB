B = int(input())

for A in range(0,B,100):
    if B == (A//10)*11:
        print(A)