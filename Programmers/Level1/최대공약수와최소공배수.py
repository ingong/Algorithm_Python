def solution(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n * m / c)]
    return answer

# def gcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x%y)

# result = gcd(2, 5)
# print(result)