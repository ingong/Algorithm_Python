n, m = map(int, input().split())
result = []


def dfs(index, start, n, m):
    if index == m:
        for i in range(0, len(result)):
            print(result[i], end=' ')
        print()
        return
    for number in range(start, n + 1):
        result.append(number)
        dfs(index + 1, number, n, m)
        result.pop()


dfs(0, 1, n, m)
