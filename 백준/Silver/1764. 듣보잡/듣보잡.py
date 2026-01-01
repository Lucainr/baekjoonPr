import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    unheard = set()
    for _ in range(n):
        unheard.add(input().strip())

    both = []
    for _ in range(m):
        name = input().strip()
        if name in unheard:
            both.append(name)

    both.sort()
    print(len(both))
    print("\n".join(both))

if __name__ == "__main__":
    main()