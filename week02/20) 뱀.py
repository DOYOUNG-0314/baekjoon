N = int(input())  # 보드 크기
K = int(input())  # 사과 개수

# 0: 빈칸, 1: 사과, 2: 뱀
board = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
          
