from collections import deque
n, m = map(int, input().split())
Max = 200000
dist = [-1 for _ in range(Max+1)]
check = [0 for _ in range(Max+1)]
q = deque()
next_queue = deque()
dist[n] = 0
check[n] = True
q.append(n)

while q:
    now = q.popleft()
    if now * 2 <= Max and not check[now*2]:
        nxt = now * 2
        dist[nxt] = dist[now]
        check[nxt] = True
        q.append(nxt)
    if now - 1 >= 0 and not check[now-1]:
        nxt = now - 1
        dist[nxt] = dist[now] + 1
        check[nxt] = True
        next_queue.append(nxt)
    if now + 1 <= Max and not check[now+1]:
        nxt = now + 1
        dist[nxt] = dist[now] + 1
        check[nxt] = True
        next_queue.append(nxt)
    if not q:
        q = next_queue
        next_queue = deque()
    if check[m]:
        break

print(dist[m])
