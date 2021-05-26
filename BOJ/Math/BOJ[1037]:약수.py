N = int(input())
numList = sorted(list(map(int, input().split())))
print(min(numList) * max(numList))