c = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
r = 0
r += c.index(input())*10
r += c.index(input())
r *= 10 ** c.index(input())
print(r)