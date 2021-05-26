N = int(input())
numList = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if numList[j] < numList[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))