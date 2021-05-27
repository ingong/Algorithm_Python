N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))

for i in range(len(numList)):
    print(numList[i], end=" ")
    if (i + 1) % M == 0:
        print()



