N = int(input())
DP = [0, 1] + [0 for _ in range(N-1)]
for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N])