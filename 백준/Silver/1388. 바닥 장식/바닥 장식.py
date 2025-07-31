import sys
from collections import deque

n, m = map(int, input().split())
room = [list(input().strip()) for _ in range(n)]
checked = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    checked[x][y] = True
    if room[x][y] == '-':
        while queue:
            cx, cy = queue.popleft()
            ny = cy + 1 # 같은 행
            if ny < m and not checked[cx][ny] and room[cx][ny] == '-':
                checked[cx][ny] = True
                queue.append((cx, ny))
    else:
        while queue:
            cx, cy = queue.popleft()
            nx = cx + 1 # 같은 열
            if nx < n and not checked[nx][cy] and room[nx][cy] == '|':
                checked[nx][cy] = True
                queue.append((nx, cy))

count = 0
for i in range(n):
    for j in range(m):
        if not checked[i][j]:
            bfs(i, j)
            count += 1

print(count)