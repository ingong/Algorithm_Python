from collections import deque
N, K = map(int, input().split())
Max = 200000
dist = [-1 for _ in range(Max)]
check = [0 for _ in range(Max)]
dist[N] = 0
q = deque()
check[N] = 1
q.append(N)
while q:
    now = q.popleft()
    for nxt in [now + 1, now - 1, now * 2]:
        if 0 <= nxt < Max and check[nxt] == False:
            check[nxt] = 1
            dist[nxt] = dist[now] + 1
            q.append(nxt)

print(dist[K])
