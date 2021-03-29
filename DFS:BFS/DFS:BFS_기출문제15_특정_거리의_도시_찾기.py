from collections import deque 
# ! 모든 도로의 거리는 1인 조건 덕분에 BFS
# 시간 복잡도 : O(N+M) 으로 동작하는 소스코드 작성
# 특정한 도시 X 를 시작점으로 BFS 수행하여 모든 도시까지의 최단거리 계산한 후에, 각 최단거리를 하나씩 확인
# 그 값이 K 인 경우 해당 도시의 번호 출력

n, m, k, x = map(int, input().split())
# 도시에 대한 정보
# 첫 번째 도시에 대한 정보가 배열의 index 1에 담기게 
graph = [[] for _ in range(n+1)]

# 모든 도로 정보
# 이중 리스트의 형태로 담는다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    

# 모든 도시에 대한 최단 거리 최소화
# distance 
distance = [-1] * (n + 1)
distance[x] = 0


q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인 
    for next_node in graph[now]:
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
            
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)

# [[], [2, 3], [3, 4], [], []]