import sys

input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 기본 튜플 정렬: 먼저 x 오름차순, x 같으면 y 오름차순
points.sort()

for x, y in points:
    print(x, y)