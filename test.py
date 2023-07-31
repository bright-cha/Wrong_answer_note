n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

a = 'BWBWB'

print(a in board[0])