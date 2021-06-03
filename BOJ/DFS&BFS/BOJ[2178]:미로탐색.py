from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 궁금한거
# count 를 어떻게 증가시킬 것인지 => dist 라는 배열을 check 와 함께 사용
# 최적 경로가 아니라면 어떻게 판단할것인지 => bfs 로 하므로 이미 보장되어있다
# 어떻게 마지막인지 아는것인지 => 그냥 마지막 배열의 요소를 구하면 된다
def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    print(dist[-1][-1])


n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
bfs(0, 0)