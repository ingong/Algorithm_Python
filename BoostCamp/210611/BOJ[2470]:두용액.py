N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
stop = False
minV = 2000000000
ans = (0, 0)

for i in range(N):
    a = i + 1
    b = N - 1
    while a <= b and not stop:
        m = (a + b) // 2
        temp = liquids[i] + liquids[m]
        if abs(temp) < minV:
            minV = abs(temp)
            ans = (liquids[i], liquids[m])
        if temp < 0:
            a = m + 1
        elif temp > 0:
            b = m - 1
        else:
            stop = True
    if stop:
        break


print(ans[0], ans[1])