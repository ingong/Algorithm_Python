from typing import List
class Solution:
    def classifyArray(self, arr: List[int]) -> str:
        ascending = True
        descending = True

        for i in range(1, 8):
            if userInput[i] > userInput[i - 1]:
                descending = False
            if userInput[i] < userInput[i - 1]:
                ascending = False

        if ascending:
            answer = "ascending"
        elif descending:
            answer = "descending"
        else:
            answer = "mixed"
        return answer

userInput = list(map(int, input().split(' ')))
solution = Solution()
result: List = solution.classifyArray(userInput)
print(result)



