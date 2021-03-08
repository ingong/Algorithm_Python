from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    # input 값을 행번 만큼 받고, 각 행에서 받은 input 값을 int 로 바꾼 후 list 에 넣어서 graph 에 append
    graph.append(list(map(int, input())))
    
    
# 1 1 0
# 0 1 0 
# 0 1 1 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))