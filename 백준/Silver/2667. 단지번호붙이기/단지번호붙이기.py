import sys
from collections import deque

input = sys.stdin.readline 

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있고, 집이 있으면서 방문 안 한 경우
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()

print(len(result))
for size in result:
    print(size)