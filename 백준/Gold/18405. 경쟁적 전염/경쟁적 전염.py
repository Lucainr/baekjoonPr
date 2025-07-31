import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

virus_data = [] # 바이러스 최초 발견시 바이러스의 정보 저장하는 리스트

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:  # 바이러스가 있ㄷ으면 virus_data에 추가
            virus_data.append((graph[i][j], 0, i, j))

virus_data.sort() # 1~k까지의 숫자로 되어있다했으니 정렬 그리고 낮은정보의 바이러스 부터 확산 시작

queue = deque(virus_data)

s, x, y = map(int, input().split()) # s초 후의 (x, y)좌표에 있는 바이러스 종류를 찾을것임

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    # 큐에서 꺼내서 각각 변수로 뽑음
    virus, time, cx, cy = queue.popleft()

    if time == s:
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0: # 범위 안에 있으면서 감염되지 않은 곳일때만
            graph[nx][ny] = virus # 해당 위치는 virus의 정수값을 가지고 있는 애한테 감염
            queue.append((virus, time + 1, nx, ny))

print(graph[x - 1][y - 1])