import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
check = [False for _ in range(n+1)]
a = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(x):
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            dfs(y)

for i in range(1, n+1):
    if check[i] == False:
        dfs(i)
        count += 1

print(count)