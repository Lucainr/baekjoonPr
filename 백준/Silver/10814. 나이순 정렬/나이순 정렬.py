import sys

input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

# 파이썬 sort는 stable이라 나이만 기준으로 정렬해도 같은 나이끼리는 입력 순서가 유지 됨
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)