from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 사과

directions = {}
for _ in range(int(input())):
    t, d = input().split()
    directions[int(t)] = d

snake = deque([(0, 0)])
board[0][0] = 2

# → ↓ ← ↑
vec = [(0,1), (1,0), (0,-1), (-1,0)]
dir = 0
time = 0

while True:
    time += 1
    x, y = snake[0]
    dx, dy = vec[dir]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
    else:
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
        tx, ty = snake.pop()
        board[tx][ty] = 0

    if time in directions:
        if directions[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

print(time)
