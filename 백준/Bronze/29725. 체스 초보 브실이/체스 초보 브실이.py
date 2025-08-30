w = 0
b = 0
for _ in range(8):
    c = input()
    w += c.count('P') + c.count('N')*3 + c.count('B')*3 + c.count('R')*5 + c.count('Q')*9
    b += c.count('p') + c.count('n')*3 + c.count('b')*3 + c.count('r')*5 + c.count('q')*9
print(w-b)