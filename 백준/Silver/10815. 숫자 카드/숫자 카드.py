import sys

input = sys.stdin.readline

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1 # 마지막 인덱스는 list의 길이보다 1 작음

    while left <= right: # 이분탐색
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

n = int(input())
cards = list(map(int, input().split()))

cards.sort()

m = int(input())
targets = list(map(int, input().split()))
# targets은 정렬 X
results = []

for target in targets:
    results.append(binary_search(cards, target))

print(' '.join(map(str, results)))