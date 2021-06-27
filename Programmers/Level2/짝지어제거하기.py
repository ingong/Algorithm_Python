def solution(s):
    stack = []
    for alpha in s:
        if not stack:
            stack.append(alpha)
        elif stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)

    if len(stack) == 0:
        return 1
    else:
        return 0