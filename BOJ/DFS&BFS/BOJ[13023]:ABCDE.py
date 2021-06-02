import sys
n, m = map(int, input().split())
edges = []
a = [[False] * n for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    # 인접 리스트
    edges.append((u, v))
    edges.append((v, u))
    # 인접 행렬
    a[u][v] = a[v][u] = True
    # 간선 리스트
    g[u].append(v)
    g[v].append(u)

m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)
#         print(A, B)
#         print(C, D)
# 1. A -> B 로 가는 모든 간선 (간선 리스트)
# 2. C -> D 로 가는 모든 간선 (간선 리스트)
# 3. B -> C (인접 행렬)
# 4. D ->