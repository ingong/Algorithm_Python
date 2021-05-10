import sys

testCase = int(sys.stdin.readline().strip())
for _ in range(testCase):
    applis = int(sys.stdin.readline().strip())

    rankList = []
    for _ in range(applis):
        rankList.append(list(map(int, sys.stdin.readline().strip().split())))
    sortedRankList = sorted(rankList, key=lambda x: x[0])

    result = 1
    minVal = sortedRankList[0][1]
    for i in range(len(sortedRankList)):
        if sortedRankList[i][1] < minVal:
            result += 1
            minVal = sortedRankList[i][1]
    print(result)

# sort 를 안쓰고, 두 개니깐 index 와 list 로 접근하게도 한다



