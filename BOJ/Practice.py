import sys
n, m = 3, 3
c = [False for _ in range(n+1)]
a = [0 for _ in range(m)]


def go(index, n):
    if index == n:
        print(a)
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n)
        c[i]= False

go(0, n)