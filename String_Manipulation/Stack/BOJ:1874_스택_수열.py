# 1. 스택에 원소를 삽입할 때는 단순히 특정 수에 도달할 때까지 삽입
# 2. 스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인

n = int(input())

count = 1
stack = []
result = []

# n 만큼 데이터 값 입력받기
for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("No")
        exit(0)

print('\n'.join(result))
