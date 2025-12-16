import sys
input = sys.stdin.readline

user_input = input().strip()
letters = [letter for letter in user_input]

e = ''
answer = ""

for letter in sorted(set(letters)):
    c = letters.count(letter)
    if c % 2 == 1:
        if e != '':
            print("I'm Sorry Hansoo")
            sys.exit()
        else:
            e = letter
    answer += letter * (c//2)
answer += e + answer[::-1]
print(answer)