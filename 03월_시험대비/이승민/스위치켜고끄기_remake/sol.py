import sys

sys.stdin = open('input.txt')
# 1~
# ON : '1', OFF : '0'
# 남학생 스위치 번호가 소수이면 , 제자리와 길이만큼 양옆 스위치 바꿈 (범위 벗어나기 전까지)
# 여학생 : 스위치 번호의 약수이면, 약수를 다 바꾼다.
# 소수 리스트
prime = [2, 3]
for i in range(4, 101):  # 스위치 개수 100, 1은 소수 아님
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lights = list(map(int, input().split()))
    M = int(input())
    studs = [list(map(int, input().split())) for _ in range(M)]
    print(lights)
    # 인덱스는 s[1] - 1
    for s in studs:
        # 남학생이이면
        if s[0] == 1:
            for i in range(2, s[1] + 1):
                if i in prime:
                    for j
        # 여학생이면
        if s[0] == 2:
            # 약수 찾기
            div = []
            # 0으로 못나누니까 1부터 시작, 자기도 약수니까 +1까지
            for i in range(1, s[1] + 1):
                if s[1] % i == 0:
                    # 약수면 추가
                    div.append(i)
            for i in div:
                lights[i - 1] = abs(lights[i - 1] - 1)

        print(j, lights)
    print(f'#{t} {lights}')
