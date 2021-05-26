N = int(input())
numList = list(map(int, input().split()))
dp = [0] * N
dp[0] = numList[0]
for i in range(1, N):
    dp[i] = max(numList[i], dp[i-1]+numList[i])
print(max(dp))
