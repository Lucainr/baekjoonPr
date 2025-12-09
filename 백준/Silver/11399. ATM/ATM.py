import sys

input = sys.stdin.readline

N = int(input().strip())
P = list(map(int, input().split()))

P.sort()  # 인출 시간이 짧은 순으로 정렬

current_sum = 0
answer = 0

for t in P:
    current_sum += t   # 지금 사람까지의 누적 시간
    answer += current_sum  # 이 사람의 대기 포함 시간 더하기

print(answer)