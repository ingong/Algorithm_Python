N = int(input())
pay = []
for _ in range(N):
    pay.append(list(map(int, input().split())))

DP = [[0 for _ in range(3)] for _ in range(N)]

DP[0][0] = pay[0][0]
DP[0][1] = pay[0][1]
DP[0][2] = pay[0][2]

for i in range(1, N):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + pay[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + pay[i][1]
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + pay[i][2]

print(min(DP[N-1]))