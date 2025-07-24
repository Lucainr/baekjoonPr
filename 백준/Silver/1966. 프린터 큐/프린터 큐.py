import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())  # n: 문서 개수, m: 궁금한 문서 위치
    impo_list = list(map(int, input().split()))  # 중요도 리스트

    queue = deque()  # (문서의 위치, 중요도)를 넣을 큐

    # 직접 인덱스를 붙여서 큐에 넣기
    for i in range(n):
        queue.append((i, impo_list[i]))

    count = 0  # 출력 순서
    
    while queue:
        now = queue.popleft()  # 맨 앞 문서 꺼냄
        # 중요도가 더 높은 문서가 뒤에 있는지 확인
        is_higher = False
        for doc in queue:
            if doc[1] > now[1]:
                is_higher = True
                break

        if is_higher:
            queue.append(now)  # 중요도 높은 문서가 있으니 다시 뒤로
        else:
            count += 1  # 인쇄됨
            if now[0] == m:  # 내가 찾는 문서면
                print(count)
                break
