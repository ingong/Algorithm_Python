import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


solution = Solution()
result: List = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)