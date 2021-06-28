# DFS 로 문제 풀기
from collections import deque
N = 5
area = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
new_area = [[1 if a > 4 else 0 for a in area[i]] for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    new_area[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            if 0 <= x - 1 < N and 0 <= x + 1 < N and 0 <= y - 1 < N and 0 <= y + 1 < N:
                nx = x + dx[i]
                ny = y + dy[i]
                if new_area[nx][ny] == 1:
                    new_area[nx][nx] = 0
                    q.append((nx, ny))


count = 0
for i in range(N):
    for j in range(N):
        if new_area[i][j] == 1:
            bfs(i, j)
            print(new_area)
            count += 1

print(count)