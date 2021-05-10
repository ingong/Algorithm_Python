import sys
from typing import List

class Solution:
    def employee(self, rankList: List[int]) -> int:
        minVal = rankList[1]
        count = 1
        for i in range(2, N+1):
            if minVal > rankList[i]:
                count += 1
                minVal = rankList[i]
        print(count)


solution = Solution()
testCase = int(sys.stdin.readline().strip())
for _ in range(testCase):
    applis = int(sys.stdin.readline().strip())
    N = applis
    rankList = [0] * (N + 1)

    for _ in range(applis):
        first, second = map(int, sys.stdin.readline().strip().split())
        rankList[first] = second
    solution.employee(rankList)



# rankList = [0] * 10
# print(rankList)