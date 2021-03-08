# DFS 메서드 정의
# 그래프, 첫 번째 넣을 요소, visited 
# 1. 현재 넣은 요소 방문 처리
# 2. for i in graph[v] -> 인접한 요소를 순회
# 3. if not visited[i] -> visited[i] = True
# 4. 겹친다 그러면 재귀 함수쓰는거지 뭐
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 0 번째 노드는 빈 리스트로 
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9
dfs (graph, 1, visited)


# BFS
# 1. queue 에 넣는다 queue = deque([start])
# 2. 방문처리한다 queue[start] = True
# 3. queue 안에 무언가가 있다면, 꺼낸다 while queue: v = queue.popleft()
# 4. 주변을 순회 for i in graph[v] 
# 5. queue 에 넣는다 queue.append(i)
# 6. 방문처리한다 visited[i] = True
from collections import deque
def bfs(graph, start, vistied):
    # ! queue = deque([start])
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            queue.append(i)
            visited[i] = True
            
    
    