n,m,k = map(int,input().split())
card_list = 'O'* m + 'X'* (n-m)
my_list = 'O'* k + 'X'* (n-k)
card_cnt = 0
for i in range(n):
    if card_list[i] == my_list[i]:
        card_cnt += 1
print(card_cnt)