from collections import deque
import sys

MAX = 200000
sys.setrecursionlimit(MAX)
check = [False] * MAX
dist = [-1] * MAX
via = [-1] * MAX
n, m = map(int, input().split())
check[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    now = q.popleft()
    for nxt in [now + 1, now - 1, now * 2]:
        if 0 <= nxt < MAX and not check[nxt]:
            check[nxt] = True
            dist[nxt] = dist[now] + 1
            via[nxt] = now
            q.append(nxt)


def go(n, m):
    if n != m:
        go(n, via[m])
    print(m, end=' ')


print(dist[m])
go(n, m)