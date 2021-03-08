# BFS : 간선의 비용이 모두 같을 때 최단 경로를 위해 사용할 수 있다
# ! 주변 상, 하, 좌, 우 한 번씩하면 되니깐 BFS 이다
# 상 하 좌 우 연결되어 있는 노드 확인
# 새로운 지점 방문 할 때 이전 노드 까지의 거리 + 1 을 넣어준다
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
#! 방향 벡터 정의
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
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))