import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
check = [False for _ in range(n)]
a = [[] for _ in range(n)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    a[u-1].append(v-1)
    a[v-1].append(u-1)

def bfs(start):
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        for y in a[x]:
            if check[y] == False:
                q.append(y)
                check[y] = True

for i in range(n):
    if check[i] == False:
        bfs(i)
        count += 1

print(count)
