# 공백을 기준으로 받아서 각각 n, m 에 넣어준다
n, m = map(int, input().split())

graph = []
for i in range(n):
    # input 값을 행번 만큼 받고, 각 행에서 받은 input 값을 int 로 바꾼 후 list 에 넣어서 graph 에 append
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 재귀 함수 dfs 
    if gr1aph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y) 
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
# 최초 진입 지점에 대해서만 result += 1 을 해줌으로써 인접 지점에 대해서 result 값 영향 받지 않는다
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
            
print(result)
            
