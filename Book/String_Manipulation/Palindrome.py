import collections

class Solution1:
    def ispalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            # 영문자, 숫자 여부를 판별하는 함수
            if char.isalnum():
                strs.append(char.lower())
        # 리스트로 했을 때와의 차이는 pop(0) -> popleft() 사용
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


solution1 = Solution1()
test_case: str = "A man, a plan, a canal: panama"
result: bool = solution1.ispalindrome(test_case)
print(result)
