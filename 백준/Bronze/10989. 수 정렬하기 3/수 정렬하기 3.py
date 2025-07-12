import sys

input = sys.stdin.readline

cnt = int(input())
count = [0] * 10001

for _ in range(cnt):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)