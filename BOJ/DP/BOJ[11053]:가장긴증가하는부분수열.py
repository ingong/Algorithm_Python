N = int(input())
numList = list(map(int, input().split()))
DP = [0] * N
v = [-1] * N
for i in range(N):
    DP[i] = 1
    for j in range(i):
       if numList[j] < numList[i] and DP[j]+1 > DP[i]:
           DP[i] = DP[j]+1
           v[i] = j

answer = max(DP)
p = [i for i,x in enumerate(DP) if x == answer][0]
print(answer)

def go(p):
    if p == -1:
        return -1
    go(v[p])
    print(numList[p], end=" ")

go(p)