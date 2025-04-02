import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]  # 위 아래
dy = [0, 0, -1, 1]  # 왼 오

def dfs(x, y):
    visited[x][y] = True
    count = 1  # 현재 집 1채 포함
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            house_count = dfs(i, j)
            result.append(house_count)

result.sort()

print(len(result))  # 단지 수
for r in result:
    print(r)