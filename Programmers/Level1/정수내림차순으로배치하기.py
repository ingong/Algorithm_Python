def solution(n):
    return "".join(sorted(list(str(n)), reverse=True))


print(solution(118372))
