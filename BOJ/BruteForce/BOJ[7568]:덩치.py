n = int(input())
hList = [list(map(int, input().split())) for i in range(n)]
result = [1] * len(hList)

for i in range(n):
    for j in range(n):
        if hList[i][0] < hList[j][0] and hList[i][1] < hList[j][1]:
            result[i] += 1

for i in result:
    print(i, end=' ')