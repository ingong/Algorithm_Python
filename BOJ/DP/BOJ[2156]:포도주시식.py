N = int(input())

drink = [0] * 10000
for i in range(N):
    drink[i] = int(input())

dp = [0] * 10000
dp[0] = drink[0]
dp[1] = drink[0] + drink[1]
dp[2] = max(drink[0] + drink[1], drink[0] + drink[2], drink[1]+drink[2])

for i in range(3, N):
    dp[i] = max(dp[i-1], dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])

print(max(dp))


