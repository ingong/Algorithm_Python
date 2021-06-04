#
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n, m = map(int, input().split())
ans = 0

for i in range(n, m + 1):
    if is_prime(i):
        print(i)


