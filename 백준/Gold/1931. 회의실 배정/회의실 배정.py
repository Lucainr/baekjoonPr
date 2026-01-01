import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    meetings = []
    for _ in range(n):
        s, e = map(int, input().split())
        meetings.append((s, e))

    # 끝나는 시간 우선, 같으면 시작 시간 우선
    meetings.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    cur_end = 0

    for s, e in meetings:
        if s >= cur_end:
            cnt += 1
            cur_end = e

    print(cnt)

if __name__ == "__main__":
    main()