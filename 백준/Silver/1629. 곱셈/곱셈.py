import sys

input = sys.stdin.readline

def reduce_pow(a, b, c):
    if b == 1:
        return a % c
    
    x = reduce_pow(a, b//2, c)
    
    if b % 2 == 0:
        return (x * x) % c     
    else:
        return a * (x * x) % c

a, b, c= map(int, input().split())

print(reduce_pow(a, b, c))