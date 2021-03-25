from typing import List
import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                        if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        print(counts)
        return max(counts, key=counts.get)
        # counts = collections.Counter(words)
        # print(counts)
        # print(type(counts))
        # return counts.most_common(1)[0][0]

solution = Solution()
result: str = solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(result)

