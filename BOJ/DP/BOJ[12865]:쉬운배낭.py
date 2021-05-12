N, K = map(int, input().split())
weights = [0] * N
values = [0] * N
for i in range(N):
    weights[i], values[i] = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N)]


def pack(idx, w):
    if idx == N:
        return 0
    if w >= K:
        return 0

    if dp[idx][w] == 0:
        v1 = 0
        if w + weights[idx] <= K:
            v1 = values[idx] + pack(idx + 1, w + weights[idx])
        v2 = pack(idx + 1, w)
        dp[idx][w] = max(v1, v2)
    return dp[idx][w]


print(pack(0, 0))
