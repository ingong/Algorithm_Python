N = int(input())
dictList = {}

for _ in range(N):
    k, v = input().split()
    dictList[k] = int(v)

newList = sorted(dictList.items(), reverse=True, key=lambda item: item[1])
print(newList[2][0])

