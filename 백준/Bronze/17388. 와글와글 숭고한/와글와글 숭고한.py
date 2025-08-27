s= list(map(int,input().split()))
m = s.index(min(s))
if sum(s) >= 100:
    print("OK")
elif m == 0:
    print('Soongsil')
elif m == 1:
    print('Korea')
else:
    print('Hanyang')
