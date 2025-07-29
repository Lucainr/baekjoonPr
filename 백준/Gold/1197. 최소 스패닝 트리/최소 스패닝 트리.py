import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

parent = {}

def make_set(x):
    parent[x] = x

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return False
    parent[rootY] = rootX
    return True

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

for i in range(1, v+1):
    make_set(i)

mst_weight = 0
cnt = 0

for a, b, c in edges:
    if union(a, b):
        mst_weight += c
        cnt += 1
        if cnt == v-1:  # MST는 V-1개의 간선에서 종료
            break

print(mst_weight)