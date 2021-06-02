answer = 0

def solution(numbers, target):
    global answer
    DFS(0, 0)
    return answer

def DFS(L, total):
    global answer
    if L == len(numbers):
        if total == target:
            answer += 1
    else:
        DFS(L+1, total + numbers[L])
        DFS(L+1, total - numbers[L])

numbers = [1, 1, 1, 1, 1]
target = 3
result = solution(numbers, target)
print(result)