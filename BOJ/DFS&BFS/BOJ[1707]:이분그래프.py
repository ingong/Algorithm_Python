# 논리 설계
# - DFS 는 True, False 를 반환한다
# - 색깔을 A(1), B(2) 로 칠한다
# 1. for 문 순회
# dfs(i, 1) 색깔을 칠하되, 이 것의 return 값이 False 라면
# ans = False 로 변경
# 2. dfs 함수
# 해당 color list 에 c 로 칠했다고 체크
# 연결된 점들을 순환
# if color[y] == 0 인데, dfs(y, 3-c) 값이 False 라면
# return False
# elif 컬러가 x, y 가 동일하면
# return False
# 이 모든 것을 통과했다면 return True
# 3. print 를 ans 에 따라서 반환


import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    color = [0 for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)

    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] == color[x]:
                return False
        return True

    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
    print('YES' if ans else 'NO')