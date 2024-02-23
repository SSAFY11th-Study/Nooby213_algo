import sys

sys.stdin = open('input.txt')


def find_mini(i, temp_sum):
    global mini
    if temp_sum > mini:
        return

    if i == N:
        if temp_sum < mini:
            mini = temp_sum
        return

    for j in range(N):
        if visited[j]:  # 방문 횟수가 남아 있다면
            visited[j] -= 1  # 방문
            find_mini(i + 1, temp_sum + board[i][j])
            visited[j] += 1  # 방문 표시 지움


T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N * N 배열 3 ≤ N ≤ 7
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [2] * N  # 2번 방문가능
    mini = 100 * N
    find_mini(0, 0)
    print(f'#{t} {mini}')
