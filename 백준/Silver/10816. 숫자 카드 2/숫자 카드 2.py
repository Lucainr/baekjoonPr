import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int, input().split()))
m = int(input().strip())
queries = list(map(int, input().split()))

cnt = Counter(cards)

print(' '.join(str(cnt[q]) for q in queries))