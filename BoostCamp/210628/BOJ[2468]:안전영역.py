def solution():
    N = 5
    target = 4
    answer = 0
    area = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
    visited = [[0 if area[i][j] > target else -1 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited, N)
                answer += 1

    return answer


# 만약 dfs 를 이 안에 넣어서 해결해야한다면, dx, dy
def dfs(x, y, visited, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 1
    stack = [(x, y)]
    while stack:
        px, py = stack.pop()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                stack.append((nx, ny))


result = solution()
print(result)