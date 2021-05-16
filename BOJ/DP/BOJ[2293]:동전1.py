N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [0] * (K+1)
dp[0] = 1
# 표를 그리면서 이해했다
for i in coins:
    for j in range(i, K+1):
        dp[j] += dp[j-i]

print(dp[K])

