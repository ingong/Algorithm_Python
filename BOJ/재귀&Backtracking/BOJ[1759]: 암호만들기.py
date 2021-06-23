def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(index, n, alpha, password):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if index == len(alpha):
        return
    go(index + 1, n, alpha, password + alpha[index])
    go(index + 1, n, alpha, password)


n, m = map(int, input().split())
alpha = sorted(input().split())
go(0, n, alpha, "")