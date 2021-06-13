N, K = 6, 3
M = list(map(int, '318542'))
# N, K = map(int, input().split())
deleteNum = K
# M = list(map(int, input()))
stack = []

for i in range(len(M)):
    while deleteNum > 0 and stack:
        if stack[-1] < M[i]:
            stack.pop()
            deleteNum -= 1
        else:
            break
    stack.append(M[i])

for i in range(N-K):
    print(stack[i], end="")

# for i in range(N):
#     while delNum > 0 and result:
#         if result[len(result) - 1] < nums[i]:
#             result.pop()
#             delNum -= 1
#         else:
#             break
#     result.append(nums[i])