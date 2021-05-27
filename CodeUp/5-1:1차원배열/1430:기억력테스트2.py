import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
qList = list(map(int, sys.stdin.readline().split()))
answerList = [0] * M

for i in range(len(qList)):
    if qList[i] in numList:
        answerList[i] = 1

print(*answerList)
