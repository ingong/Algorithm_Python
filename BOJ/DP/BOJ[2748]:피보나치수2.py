def Fib(n):
    if num[n] == 0 and n != 0:
        num[n] = Fib(n-1) + Fib(n-2)
    return num[n]


N = int(input())
num = [0, 1] + [0] * N
Fib(N)
print(num[N])