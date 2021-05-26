N = int(input())
li = [(i+1) for i in range(0, N)]
numList = sorted(list(int(input()) for _ in range(N-1)))
count = 0

for i in range(len(numList)):
    if li[i] != numList[i]:
        count = 1
        print(li[i])
        break


if count == 0:
    print(li[-1])

