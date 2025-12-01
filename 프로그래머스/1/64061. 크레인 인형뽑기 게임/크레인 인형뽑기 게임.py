'''
자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다.
바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

가장 최근에 들어온 값과 비교 해야함
LIFO

return 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수
board stacks moves basket c value_temp N
스택은 collections의 deque로 구현

1.보드를 popleft할수 있게 스택들의 모음로 만든다
	board의 리스트를 순회하면서 인덱스의 맞는 스택에 append해주면 먼저 들어온값이 제일 앞에 있게 되있음
2. for 문으로 moves의 값들을 한번씩 반복한다
3. moves에 맞는 스택에서 popleft을 해서 basket에 top과 비교 한다
	 moves에 맞는 스택에서 popleft을 한값을 value_temp에 일시 저장
	스택의 길이가 0일시를 대비한 예외처리를 해야함
	basket의 길이가 0일시를 대비한 예외처리를 해야함
4. basket의 top과 같을시 basket을 popleft()하고 c를 1올리고 다를시 basket에 스택에서 popleft한값 appendleft()

board	moves	result
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4
'''

from collections import deque

def solution(board, moves):
    N = len(board) # board의 길이
    # print(N)
    c = 0 # 사라진 인형의 개수
    
    stacks = [deque([]) for _ in range(N)] # 스택 모음
    # print(stack_dumy)
    basket = deque() # 바구니
    
    for col in range(N): # board를 이용해 stack_dumy만들기용해 stack_dumy만들기
        for row in range(N):
            if board[row][col] == 0:
                continue
            else:
                # print(board[j][i])
                stacks[col].append(board[row][col])
    # print(stack_dumy)
    
    for move in moves: # moves를 이용하여 입형 뽑기
        if len(stacks[move-1]) > 0:
            value_temp = stacks[move-1].popleft()
            if len(basket) > 0 and value_temp == basket[0]:
                basket.popleft()
                c += 2
            else:
                basket.appendleft(value_temp)
        
    return c

