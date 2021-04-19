from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

solution = Solution()
test_case: List = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6"]
result: List = solution.reorderLogFiles(test_case)
print(result)

