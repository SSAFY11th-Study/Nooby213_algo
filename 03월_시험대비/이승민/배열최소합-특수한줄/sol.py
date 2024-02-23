import sys

sys.stdin = open('input.txt')


# 세로 같은 줄에서 2개이상 숫자 못고름
# 특수한 줄에서 마음껏 고를 수 있다.
# 최소합 출력
def find_mini(i, temp_sum):
    global mini
    if temp_sum > mini:
        return

    if i == N:
        if temp_sum < mini:
            mini = temp_sum
        return

    for j in range(N):
        if i in M_lst:  # i 가 특수줄이면 전부 방문
            find_mini(i + 1, temp_sum + board[i][j])
        elif visited[j]:
            visited[j] = 0
            find_mini(i + 1, temp_sum + board[i][j])
            visited[j] += 1


T = int(input())
for t in range(1, T + 1):
    # N * N , M 개의 특수 줄
    # 3 <= N <= 10, 1 <= M <= N
    N, M = map(int, input().split())
    # 특수줄 M 리스트
    M_lst = list(map(int, input().split()))
    for m in range(M):
        M_lst[m] -= 1
    # 배열 표
    board = [list(map(int, input().split())) for _ in range(N)]
    # 방문표
    visited = [1] * N
    # 10 이하의 자연수 N줄이기 때문에
    mini = 10 * N

    find_mini(0, 0)
    print(f'#{t} {mini}')
