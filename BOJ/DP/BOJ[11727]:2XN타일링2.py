N = int(input())
dp = [0, 1, 2] + [0] * (N-2)

def makeTile(N):
    for i in range(3, N+1):
        dp[i] = dp[i-1] + * dp[i-2]
    return dp[N] % 10007

print(makeTile(N))

