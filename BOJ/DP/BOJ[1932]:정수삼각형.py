# 논리설계
# 1. D[i][j] = max(D[i-1][j-1], D[i-1][j]) + T[i][j]
# DP 문제는 해당 식에서 i, j 가 무엇을 의미하는지 적는다
# 해당 요소가 없다면 어떤 식으로 정의되는지를 적는다
# 이 때 범위에 유의해서 적는다

# 코드 구현
# D 라는 배열 중 해당 index 의 삼각형이 존재하지 않는다면 최소값을 넣어줌으로써 최대값을 산출하는 조건에 부합하게 만든다
# i, j 가 존재하지 않는 경우에는 pass
# D 라는 배열의 맨 마지막 index 에서 최대값을 산출한다

N = int(input())
T = []
D = [[0 for _ in range(j)] + [-10**9 for _ in range(N-j)] for j in range(1, N+1)]


for _ in range(N):
    T.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1):
        if i < 1 and j < 1:
            pass
        D[i][j] = max(D[i-1][j-1], D[i-1][j]) + T[i][j]

print(max(D[-1]))