from typing import List

class Solution:
    ## 브루트 포스로 계산
    # pseudo
    # for i in nums 배열
        # for j from i + 1 to nums 배열 마지막
            # if nums 의 두 요소의 합 == target
                # return index 를 배열의 형태로
    # 시간 복잡도 : n 제곱
    def twoSum1(self, nums: List[int], target: int ) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    ## in 을 이용한 탐색
    # pseudo
    # for 인덱스, 값 in enumerate(nums):
        # 타겟에서 해당 요소 뺀 값
            # if 뺀 값 in nums from i+1 to 배열의 끝
                # return index
    # enumerate 에 대해서 공부하자!!!
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

    # 첫 번째 수를 뺀 결과 키 조회 : dict 키와 value 를 바꿔준
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


solution = Solution()
# test_case
nums: List = [2, 7, 11, 15]
target: int = 9
result: List = solution.twoSum5(nums, target)
print(result)