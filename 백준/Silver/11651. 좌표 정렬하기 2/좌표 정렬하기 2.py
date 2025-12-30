import sys

input = sys.stdin.readline

n = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(n)]

# y 오름차순, y가 같으면 x 오름차순
points.sort(key=lambda p: (p[1], p[0]))

out = []
for x, y in points:
    out.append(f"{x} {y}")
sys.stdout.write("\n".join(out))