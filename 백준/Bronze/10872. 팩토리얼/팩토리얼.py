def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

num = int(input())
print(factorial(num))