from typing import List

class Solution:
    def waitDaysforwarm(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)
        for i, cur in enumerate(T):
            while stack and T[stack[-1]] < cur:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

solution = Solution()
T: List = [73, 74, 75, 71, 69, 72, 76, 73]
result: List = solution.waitDaysforwarm(T)
print(result)

# 문제 포인트
# 1. index 값을 stack 에 넣어준다
# 2. 탑 문제랑 거의 동일

# 내가 놓친 포인트
# 1. answer = [0] * len(T)
# 2. enumerate 활용
# 3. stack.pop() 의 값을 last 라는 변수를 선언해서 할당
# 4. from typing import List