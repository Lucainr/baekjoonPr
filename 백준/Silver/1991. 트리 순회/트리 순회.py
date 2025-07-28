import sys

input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# 전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])
# 후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])    # 왼쪽 자식 순회
    postorder(tree[node][1])    # 오른쪽 자식 순회
    print(node, end='')         # 현재 노드 출력

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()