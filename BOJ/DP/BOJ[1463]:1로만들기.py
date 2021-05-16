N = int(input())
dp = [0, 0, 1, 1]

def makeOne(N):
    for i in range(4,N+1):
        dp.append(dp[i - 1] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i // 3]+1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i // 2]+1, dp[i])
    return dp[N]

print(makeOne(N))