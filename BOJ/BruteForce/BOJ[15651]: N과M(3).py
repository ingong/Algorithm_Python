n, m = map(int, input().split())
result = []


def dfs(index, n, m):
    if index == m:
        for i in range(0, len(result)):
            print(result[i], end=' ')
        print()
        return
    for number in range(1, n + 1):
        result.append(number)
        dfs(index + 1, n, m)
        result.pop()


dfs(0, n, m)
