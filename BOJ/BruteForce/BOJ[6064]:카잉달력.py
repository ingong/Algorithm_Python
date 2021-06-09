# 일부만 해도 정답을 구하는 경우가 있다
# x 를 이용해 모든 해를 고려하지 않고
n = int(input())
for _ in range(n):
    N, M, x, y = map(int, input().split())
    if x > N or y > M:
        print(-1)
        continue

    a = 1
    b = 1
    answer = 1

    while a != x or b != y:
        if a > N:
            a = 1
        if b > M:
            b = 1

        if answer > N * M:
            answer = -1
            break
        a += 1
        b += 1
        answer += 1

    print(answer)
