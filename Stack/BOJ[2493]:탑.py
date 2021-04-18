import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0] * len(arr)
stack = []

for i in range(len(arr)-1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = i + 1
    stack.append(i)
print(*answer)

# 알아둬야할 포인트
# 1. arr 을 역순으로 접근
# 2. stack 에 push 하는 요소를 index 로 지정
# 3. stack 에 대해서 pop 하는 요소와 answer 의 index 에 해당 값을 넣어준다
# 4. answer 을 미리 0 으로 채워넣는다

# 내가 이해한 코드의 의도
# sys.stdin.readline() 으로 받을 때도 int 라는 자료형 지정해줘야해
# stack 의 최상단요소가 지금 arr[i] 보다 작으면 stack 에서 이를 빼내고, answer[stack.pop()]에 해당 index + 1 값을 넣어준다
# while 문을 통해 stack 내부에 요소가 있고 해당 조건을 또 만족한다면 stack[-1] 에 해당하는 index 에 대한 answer 에 값을 넣어준다
