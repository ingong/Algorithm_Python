n, m = map(int, input().split())
c = [False] * (n + 1)
a = [0] * m
s = 1

def go(index, n, m, s):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(s, n + 1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        s = i
        go(index + 1, n, m, s)
        c[i] = False


go(0, n, m, s)
