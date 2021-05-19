N = int(input())
cardList = list(map(int, input().split()))
dp = [0] * N

for idx, val in enumerate(cardList):
    dp[idx] = cardList[idx]
    k = (idx//2) + 1
    for i in range(0, k):
        dp[idx] = min(dp[idx], dp[idx-1-i] + dp[i])

print(dp[N-1])