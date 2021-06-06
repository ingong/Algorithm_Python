def solution(num):
    return list(filter(lambda x: num % x == 0, range(1, num + 1)))


result = solution(0)
print(result)