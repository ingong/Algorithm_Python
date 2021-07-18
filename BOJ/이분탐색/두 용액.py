N = int(input())
properties = list(map(int, input().split()))
properties.sort()
minV = 2000000000
ans = (0, 0)
stop = False

for i in range(N-1):
    a = i + 1
    b = N - 1
    while a <= b and not stop:
        m = (a + b) // 2
        tmp = properties[i] + properties[m]
        if minV > abs(tmp):
            ans = (properties[i], properties[m])
            minV = abs(tmp)
        if tmp < 0:
            a = m + 1
        elif tmp > 0:
            b = m - 1
        else:
            stop = True
    if stop:
        break


print(ans[0], ans[1])