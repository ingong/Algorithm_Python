def dfs(L, total, arr, visited):
    if L == len(arr):
        if not visited[total] and 0 < total <= sum(arr):
            visited[total] = True
    else:
        dfs(L + 1, total + arr[L], arr, visited)
        dfs(L + 1, total - arr[L], arr, visited)
        dfs(L + 1, total, arr, visited)

    return visited


N = int(input())
arr = list(map(int, input().split()))
L = 0
total = 0
visited = [False for _ in range(sum(arr) + 1)]
answer = dfs(L, total, arr, visited)
print(answer.count(False) - 1)
