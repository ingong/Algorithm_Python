N = int(input())
numList = list(map(int, input().split()))
DP = [0] * N

for i in range(N):
    DP[i] = 1
    for j in range(i):
       if numList[j] < numList[i] and DP[j]+1 > DP[i]:
           DP[i] = DP[j]+1

print(max(DP))