import math

def solution(n):
    if n % math.sqrt(n) == 0:
        return (round(math.sqrt(n))) ** 2
    else:
        return -1


print(solution(121))