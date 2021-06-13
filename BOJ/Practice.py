from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

MAX = 200000
dist = [-1 for _ in range(MAX)]
check = [False for _ in range(MAX)]
via = [0 for _ in range(MAX)]

N, K = map(int, input().split())
q = deque()
q.append(N)
dist[N] = 0
check[N] = True

while q:
    now = q.popleft()
    for nex in [now + 1, now - 1, now * 2]:
        if 0 <= nex < MAX and not check[nex]:
            dist[nex] = dist[now] + 1
            check[nex] = True
            via[nex] = now
            q.append(nex)


def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end=' ')


print(dist[K])
go(N, K)



