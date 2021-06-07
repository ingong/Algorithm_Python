from functools import reduce

def solution(num):
    return list(filter(lambda x: num % x == 0, range(1, num + 1)))


for i in range(1, 1):
    print(i)

print(reduce(lambda x, y: x + y, range(5)))
