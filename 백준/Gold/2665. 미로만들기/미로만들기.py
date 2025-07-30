import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == n-1:
            return visited[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr[nx][ny] == '1':
                    queue.appendleft((nx, ny))  # 흰 방은 가중치 0
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))      # 검은 방은 가중치 1
                    visited[nx][ny] = visited[x][y] + 1
                    
print(bfs())