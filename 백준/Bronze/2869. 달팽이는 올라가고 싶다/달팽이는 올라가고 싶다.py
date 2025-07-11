import math

A, B, V = map(int, input().split())

need = V - A
daily = A - B

if need % daily == 0:
    days = need // daily
else:
    days = need // daily + 1

print(days + 1)