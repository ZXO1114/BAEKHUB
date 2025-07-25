distance = int(input())
minute = distance // 5
if distance % 5 != 0:
    minute += 1
print(minute)