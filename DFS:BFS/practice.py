def solution(prices):
    stack = []
    answer = []
    for i in range(len(prices) - 1, -1, -1):
        answer.append(i)

    for i, cur in enumerate(prices):
        while stack and prices[i] < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer


result = solution([1, 2, 3, 2, 3])
print(result)