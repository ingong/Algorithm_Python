n, m = map(int, input().split())
check = [False] * (n + 1)
cnt = [0] * m
selected = 1


def go(index, n, m, selected):
    if index == m:
        print(' '.join(map(str, cnt)))
        return
    for i in range(selected, n + 1):
        selected = i
        cnt[index] = i
        go(index + 1, n, m, selected)


go(0, n, m, selected)
