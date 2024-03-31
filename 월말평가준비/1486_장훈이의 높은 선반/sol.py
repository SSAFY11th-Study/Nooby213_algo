import sys
sys.stdin = open('input.txt')

def top(n, sum_height):
    global mini

    if sum_height < B:
        return

    if sum_height - B > mini:
        return

    if mini == 0:
        return

    mini = min(mini, sum_height - B)


    for i in range(n, N):
        if visited[i] == 0:
            visited[i] = 1
            top(n + 1, sum_height - clerk[i])
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    # 높이 B 선반
    # N 명의 점원
    # 1 ≤ N ≤ 20, 1 ≤ B ≤ S
    N, B = map(int, input().split())
    clerk = []
    mini = 0
    sum_all = 0
    for i in input().split():
        clerk.append(int(i))
        sum_all += int(i)
    mini = sum_all - B
    visited = [0] * N
    clerk.sort()
    top(0, sum_all)
    print(f'#{t} {mini}')