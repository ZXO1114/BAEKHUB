dc = int(input())//5
v = int(input())
match dc:
    case 0 :
        pass
    case 1:
        v -= 500
    case 2:
        if (v*90/100) <= (v-500): v *= (90/100)
        else: v -= 500
    case 3:
        if (v - 2000) <= (v * 90 / 100): v -= 2000
        else: v *= (90/100)
    case _:
        if (v * 75 / 100) <= (v - 2000): v *= (75 / 100)
        else: v -= 2000
if v <= 0:
    print(0)
else:
    print(int(v))