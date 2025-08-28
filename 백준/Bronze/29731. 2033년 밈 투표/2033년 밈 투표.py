g = '''
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna stop
'''
n = int(input())
for i in range(n):
    if input() not in g:
        print('Yes')
        break
    if i == n-1:
        print('No')

