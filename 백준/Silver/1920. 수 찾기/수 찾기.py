import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
check_data = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

for num in check_data:
    if binary_search(data, num):
        print(1)
    else:
        print(0)